# Ping Sweeper – Scan a Subnet for Active Devices

## Overview

This tool allows users to scan a subnet for active devices using ICMP (ping) and Nmap. It helps network administrators and security professionals discover connected devices in a given network range.

## Features

- Scan a subnet for active hosts using ICMP ping.
- Perform a deeper scan using Nmap for additional details.
- Export results to a log file.
- Display results in JSON format for easy integration.

## Installation

Ensure you have Python installed, then install required dependencies:

```bash
pip install python-nmap
```

Also, ensure Nmap is installed on your system:

```bash
sudo apt install nmap  # For Debian/Ubuntu
brew install nmap      # For macOS
choco install nmap     # For Windows (using Chocolatey)
```

## Usage

Run the script using the command:

```bash
sudo python ping_sweeper.py --subnet 192.168.1.0/24
```

### Additional Options

- Perform an Nmap scan for detailed information:
  ```bash
  sudo python ping_sweeper.py --subnet 192.168.1.0/24 --nmap
  ```
- Save results to a log file:
  ```bash
  sudo python ping_sweeper.py --subnet 192.168.1.0/24 --log
  ```
- Output results in JSON format:
  ```bash
  sudo python ping_sweeper.py --subnet 192.168.1.0/24 --json
  ```

## Example Output

```bash
[+] Active Devices in 192.168.1.0/24
192.168.1.1 - Online
192.168.1.10 - Online
192.168.1.15 - Online
```

## Logging Feature

The script can save results in a `ping_sweeper.log` file for analysis.

## License

This project is licensed under the MIT License.
