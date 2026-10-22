import socket
import time

# targeting localhost for safe testing
TARGET_HOST = "127.0.0.1"

# Common ports
# 21: FTP, 22: SSH, 80: HTTP, 443: HTTPS, 8080: Alt HTTP
PORTS_TO_SCAN = [21, 22, 80, 443, 8080]

def scan_ports():
    print(f"--- STARTING PORT SCAN ON: {TARGET_HOST} ---")
    start_time = time.time()

    for port in PORTS_TO_SCAN:
        # creating a socket object
        # AF_NET = IPv4, SOCK_STREAM = TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(1.0) # setting timeout so script doesn't get stuck on close ports

        try:
            result = s.connect_ex((TARGET_HOST, port)) # returns 0 if connection was successful (Port is Open)

            if result == 0:
                print(f"[OPEN] Port {port} is active.")
            else:
                print(f"[CLOSED] Port {port}")

        except socket.error:
            print(f"[ERROR] Clould not connect to port {port}")
        # closing the socket to clean the system (ALWAYS)
        finally:
            s.close()

    duration = time.time() - start_time
    print(f"\nScan complete in {duration:.2f} seconds.")
    

if __name__ == "__main__":
    scan_ports()