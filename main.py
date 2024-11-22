import argparse
import requests
import socket
import time
from requests.exceptions import RequestException

# Definindo headers comuns a serem reutilizados em todas as requisições
COMMON_HEADERS = {
    'Host': '192.168.100.1',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://192.168.100.1',
    'Referer': 'http://192.168.100.1/deviceOperation.html',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': '__session:0.09721598418207011:conn_mode=0; __session:0.09721598418207011:net_mode=0; __session:0.09721598418207011:imei=860018046097359; __session:0.09721598418207011:fwversion=UZ801-V2.3.10; __session:mainifr:conn_mode=0;'
}

def send_request(url, data, action_description="action"):
    try:
        response = requests.post(url, headers=COMMON_HEADERS, data=data, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to {action_description}: HTTP {response.status_code}")
            return None
    except RequestException as e:
        print(f"RequestException during {action_description}: {e}")
        return None

def toggle_connection(mode):
    url = "http://192.168.100.1/ajax"
    data = f'{{"funcNo":1004,"conn_mode":"{mode}"}}'
    send_request(url, data, "toggle connection")

def restart_modem():
    url = "http://192.168.100.1/ajax"
    data = '{"funcNo":1013}'
    send_request(url, data, "restart modem")
    time.sleep(160)  # Espera o modem reiniciar

def change_ip():
    toggle_connection('1')  # Desconecta
    time.sleep(10)  # Aumentado para 10 segundos
    toggle_connection('0')  # Conecta
    time.sleep(20)  # Adiciona espera para estabelecer conexão
    return get_network_info()

def fetch_ip_info(retry_count=5):  # Aumentado para 5 tentativas
    """ Tenta obter informações do IP do ipinfo.io com tentativas. """
    url = 'https://ipinfo.io/json'
    for attempt in range(retry_count):
        try:
            time.sleep(5 if attempt > 0 else 0)  # Espera entre tentativas
            response = requests.get(url, timeout=10)  # Aumentado timeout
            if response.status_code == 200:
                return response.json()
        except (requests.ConnectionError, requests.Timeout) as e:
            print(f"Tentativa {attempt + 1}/{retry_count}: Erro de conexão: {e}")
    print("Falha ao obter informações do IP após todas as tentativas.")
    return {}

def get_network_info():
    max_retries = 3
    for attempt in range(max_retries):
        try:
            time.sleep(5 if attempt > 0 else 0)
            
            # Informações do modem local
            local_url = 'http://192.168.100.1/ajax'
            local_data = '{"funcNo":1002}'
            local_info = send_request(local_url, local_data, "buscar informações do dispositivo local")
            
            if not local_info:
                raise Exception("Não foi possível obter informações locais do modem")
            
            # Informações da rede pública com tentativas
            public_info = fetch_ip_info()
            
            # Reorganiza as informações evitando redundância
            network_info = {
                "IP Público": public_info.get('ip', 'Não disponível'),
                "Rede": public_info.get('org', 'Não disponível'),
                "Localização": f"{public_info.get('city', 'Não disponível')}, {public_info.get('region', 'Não disponível')}",
                "Rede Local": local_info.get('results', [{}])[0].get('wlan_ip', 'Não disponível'),
                "DNS": local_info.get('results', [{}])[0].get('dns1', 'Não disponível')
            }
            
            # Remove valores vazios ou 'Não disponível'
            return {k: v for k, v in network_info.items() if v and v != 'Não disponível'}
            
        except Exception as e:
            print(f"Tentativa {attempt + 1}/{max_retries}: Erro ao buscar informações de rede: {e}")
            if attempt == max_retries - 1:
                return None
            time.sleep(5)

def cli():
    parser = argparse.ArgumentParser(description="Network Management CLI")
    parser.add_argument("--interval", type=int, default=60, help="Interval in seconds between IP changes or restarts")
    parser.add_argument("--mode", type=str, default="change_ip", choices=["change_ip", "restart_modem"], help="Operation mode: change_ip or restart_modem")

    args = parser.parse_args()

    while True:
        if args.mode == "change_ip":
            info = change_ip()
        elif args.mode == "restart_modem":
            restart_modem()
            info = get_network_info()
        
        print(info)  # Print the fetched information
        print(f"--------------------- Next operation in {args.interval} seconds ---------------------")
        time.sleep(args.interval)

if __name__ == "__main__":
    cli()
