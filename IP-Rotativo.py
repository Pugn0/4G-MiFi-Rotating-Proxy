import requests
import time
from requests.exceptions import RequestException
import socket
import json

def restart_modem():
    url = "http://192.168.100.1/ajax"
    headers = {
        'Host': '192.168.100.1',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://192.168.100.1',
        'Referer': 'http://192.168.100.1/deviceOperation.html',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': '__session:0.09721598418207011:conn_mode=0; __session:0.09721598418207011:net_mode=0; __session:0.09721598418207011:imei=860018046097359; __session:0.09721598418207011:fwversion=UZ801-V2.3.10; __session:mainifr:conn_mode=0; __session:mainifr:=http:'
    }
    data_restart = '{"funcNo":1013}'
    data_status = '{"funcNo":1002}'

    # Envia comando de reinicialização
    try:
        requests.post(url, headers=headers, data=data_restart, timeout=5)
    except RequestException:
        pass  # Ignora erros aqui porque a conexão provavelmente será perdida

    # Aguarda um tempo para o modem reiniciar
    time.sleep(160)  # Ajuste este tempo conforme necessário

    # Tenta obter o status do modem após a reinicialização
    while True:
        try:
            response = requests.post(url, headers=headers, data=data_status, timeout=5)
            if response.status_code == 200:
                data = response.json()
                print(f"IP FISICO: {data['results'][0]['IP']}")  # Imprime apenas o IP
                break  # Sai do loop após conseguir o IP
        except RequestException:
            pass  # Ignora exceções e tenta novamente

        time.sleep(30)  # Intervalo entre as tentativas


def desconectar():
    url = "http://192.168.100.1/ajax"
    headers = {
        'Host': '192.168.100.1',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://192.168.100.1',
        'Referer': 'http://192.168.100.1/deviceOperation.html',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': '__session:0.09721598418207011:conn_mode=0; __session:0.09721598418207011:net_mode=0; __session:0.09721598418207011:imei=860018046097359; __session:0.09721598418207011:fwversion=UZ801-V2.3.10; __session:mainifr:conn_mode=0; __session:mainifr:=http:'
    }
    data_restart = '{"funcNo":1004,"conn_mode":"1"}'

    # Envia comando de reinicialização
    try:
        requests.post(url, headers=headers, data=data_restart, timeout=5)
    except RequestException:
        pass  # Ignora erros aqui porque a conexão provavelmente será perdida

def conectar():
    url = "http://192.168.100.1/ajax"
    headers = {
        'Host': '192.168.100.1',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://192.168.100.1',
        'Referer': 'http://192.168.100.1/deviceOperation.html',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': '__session:0.09721598418207011:conn_mode=0; __session:0.09721598418207011:net_mode=0; __session:0.09721598418207011:imei=860018046097359; __session:0.09721598418207011:fwversion=UZ801-V2.3.10; __session:mainifr:conn_mode=0; __session:mainifr:=http:'
    }
    data_restart = '{"funcNo":1004,"conn_mode":"0"}'

    # Envia comando de reinicialização
    try:
        requests.post(url, headers=headers, data=data_restart, timeout=5)
    except RequestException:
        pass  # Ignora erros aqui porque a conexão provavelmente será perdida


def get_network_info():
    try:
        # Obter IP público e outras informações usando ipinfo.io
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        
        public_ip = data.get('ip', 'Não disponível')
        location = data.get('loc', 'Não disponível')  # Latitude e Longitude
        city = data.get('city', 'Não disponível')
        region = data.get('region', 'Não disponível')
        country = data.get('country', 'Não disponível')
        isp = data.get('org', 'Não disponível')  # Organização/ISP
        
        # O IP interno pode ser útil
        local_ip = socket.gethostbyname(socket.gethostname())

        # Requisição específica para o dispositivo local
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': '__session:0.5018566057943141:conn_mode=0; __session:0.5018566057943141:net_mode=0; __session:0.5018566057943141:imei=860018046097359; __session:0.5018566057943141:fwversion=UZ801-V2.3.10; __session:mainifr:conn_mode=0',
            'Origin': 'http://192.168.100.1',
            'Referer': 'http://192.168.100.1/main.html',
            'Sec-GPC': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        local_response = requests.post('http://192.168.100.1/ajax', headers=headers, data='{"funcNo":1001}', verify=False)
        local_data = local_response.json()
        
        return {
            "Public IP": public_ip,
            "Local IP": local_ip,
            "Location": f"{city}, {region}, {country} ({location})",
            "ISP": isp,
            "Local Device Info": local_data
        }
    except Exception as e:
        return None
    
def trocaIP():
    desconectar()
    conectar()
    while True:
        ip = get_network_info()
        if ip == None:
            time.sleep(10)
        else:
            print(ip)
            break
if __name__ == "__main__":
    trocaIP()
    