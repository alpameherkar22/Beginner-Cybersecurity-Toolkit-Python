import socket
import os

# targeting a safe public domain or local placeholder to scan
TARGET_DOMAIN = "example.com"
WORDLIST_FILE = "subdomains.txt"

def enumerate_subdomains():
    if not os.path.exists(WORDLIST_FILE):
        print(f"[ERROR] Could not find {WORDLIST_FILE}")
        return

    print(f"--- STARTING SUBDOMAIN ENUMERATION ON: {TARGET_DOMAIN} ---")

    with open(WORDLIST_FILE, "r") as f:
        for line in f:
            subdomain = line.strip()

            # skipping empty lines or comments
            if not subdomain or subdomain.startswith("#"):
                continue

            full_domain = f"{subdomain}.{TARGET_DOMAIN}"

            try:
                ip_address = socket.gethostbyname(full_domain) # socket.gethostbyname attempts to resolve domain to an IP address
                print(f"[FOUND] {full_domain} ---> {ip_address}")

            except socket.gaierror: # gaierror means the domain name does not resolve (doesn't exist)
                pass

            except Exception as e:
                print(f"[ERROR] {full_domain}: {e}")

    print("\n--- ENUMERATION COMPLETE ---")

if __name__ == "__main__":
    enumerate_subdomains()