# QR Code Reader Project Readme

## Overview
This project is aimed at creating a network QR code reader using Raspberry Pi devices connected to the same WiFi network. The QR code reader periodically scans IP addresses within the network to check if they are up or down. The status of each QR code reader is recorded in a database, with a value of '1' indicating the QR code reader is up and '0' indicating it is down. Additionally, the script is configured to send an email notification in case of a loss of connection to any QR code reader.

## Features
- Ping-based QR code reader to monitor the availability of devices within the network.
- Database integration to record the status of each QR code reader.
- Email notification system for loss of connection events.

## Requirements
- Raspberry Pi devices connected to the same WiFi network.
- Python 3.x installed on each Raspberry Pi.
- Required Python packages (e.g., `sqlite3`, `smtplib`, `socket`, `subprocess`).

## Setup
1. Clone the repository to your Raspberry Pi devices.
    ```bash
    git clone https://github.com/your_username/qr-code-reader-project.git
    ```
2. Install the necessary Python packages if not already installed.
    ```bash
    pip install -r requirements.txt
    ```
3. Configure the database settings in `config.py` file.
4. Edit the list of IP addresses to scan in the `qr_code_reader.py` script.
5. Run the `qr_code_reader.py` script on each Raspberry Pi.
    ```bash
    python qr_code_reader.py
    ```

## Usage
- The `qr_code_reader.py` script can be run manually or automated using a scheduler (e.g., `cron`) to periodically scan the network.
- View the database to monitor the status of each QR code reader.
- Check email notifications for any loss of connection events.

## Troubleshooting
- Ensure all Raspberry Pi devices are connected to the same WiFi network.
- Double-check the IP addresses configured in the `qr_code_reader.py` script.
- Verify the SMTP settings for sending email notifications in the `config.py` file.

## Author
- **Prudence Radebe**
- Email: [missphumy@gmail.com](mailto:missphumy@gmail.com)

## Contributing
Contributions to improve the project are welcome! Feel free to fork the repository and submit pull requests with your enhancements.

## License
This project is licensed under the [MIT License](LICENSE).
