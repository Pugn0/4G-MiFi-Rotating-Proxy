# 4G MiFi Rotating Proxy

This project provides a Command Line Interface (CLI) tool for managing and automating IP rotation and modem restarts for 4G MiFi devices. It's ideal for applications requiring IP rotation for tasks such as web scraping, automated testing, or any other activity that benefits from frequent IP changes.

## Features

- **IP Rotation**: Automates the process of disconnecting and reconnecting the modem to acquire a new IP.
- **Modem Restart**: Enables scheduled restarting of the modem to ensure connection stability.
- **Flexible Configuration**: Allows adjusting the interval between actions via a command-line interface.

## Prerequisites

Before you begin, ensure that you:
* Have installed Python 3.6 or higher.
* Have a 4G MiFi modem configured and accessible on your local network.

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/Pugn0/4G-MiFi-Rotating-Proxy.git
```
```bash
cd 4G-MiFi-Rotating-Proxy
```
```bash
pip install -r requirements.txt
```

## Usage

To use the tool, run the following command in the terminal:

```bash
python main.py --interval <seconds_interval> --mode <change_ip|restart_modem>
```

- `<seconds_interval>`: Time interval between IP change or modem restart operations.
- `<change_ip|restart_modem>`: Choose between changing the IP or restarting the modem.

## Contributing

Contributions are welcome! If you have a suggestion that could improve this, fork the repository and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact

- **GitHub**: [Pugn0](https://github.com/Pugn0)
- **Telegram**: [@pugno_yt](https://t.me/pugno_yt)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Explanation

- **Contact Section**: This section now includes direct links to both your GitHub profile and your Telegram contact. This will allow users to reach out to you through their preferred method, be it directly through GitHub or through a more immediate platform like Telegram.
