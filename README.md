# 🛡️ Python Cybersecurity Toolkit

A collection of custom, foundational cybersecurity and network-reconnaissance tools built from scratch using Python's standard libraries and core networking modules. 

The goal of this project was to move past passive theory and manually code security mechanics—such as network sniffing, socket programming, cryptographic hashing, and automated log analysis—to deeply understand how security tools operate under the hood.

---

## 📂 Included Projects

| # | Project Name | Description | Key Modules Used |
|---|---|---|---|
| **01** | **Log Parser (SIEM-lite)** | Parses server log files, identifies high error thresholds or suspicious activity, and exports findings to CSV/JSON. | `re`, `csv`, `json`, `datetime` |
| **02** | **File Integrity Monitor** | Computes and tracks cryptographic SHA-256 hashes of files to detect unauthorized tampering or modifications. | `hashlib`, `os`, `json` |
| **03** | **Directory Brute-Forcer** | Performs web reconnaissance by testing common directory paths against a target web server and filtering by HTTP status codes. | `urllib.request`, `urllib.error` |
| **04** | **ARP Spoof Detector** | Listens to live local network traffic via Scapy to detect potential ARP poisoning / Man-in-the-Middle attacks. | `scapy`, `Npcap` |
| **05** | **TCP Port Scanner** | Scans target IP addresses across specified ports using raw TCP socket connections to identify active services. | `socket`, `time` |
| **06** | **Custom File Encryptor** | Implements a repeating-key XOR byte manipulation cipher to protect sensitive files at rest with confidentiality. | `os`, binary I/O |
| **07** | **DNS Subdomain Enumerator** | Queries DNS records using socket lookups combined with a wordlist to discover hidden subdomains and endpoints. | `socket`, `os` |

---

## ⚙️ Prerequisites & Setup

Ensure you have **Python 3.12+** installed on your system. 

For the network packet analysis tool (Project 4), ensure you have **Npcap** installed on Windows (with WinPcap API-compatible mode enabled) and Scapy:
```powershell
python -m pip install scapy