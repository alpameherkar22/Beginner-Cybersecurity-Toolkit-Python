from scapy.all import sniff, ARP

# dictionary to store known IP-MAC mappings
ip_mac_mapping = {}

def process_packet(packet):
    # checking if packet has an ARP layer
    if packet.haslayer(ARP):
        if packet[ARP]. op == 2: # ARP op=2 means it's an ARP reply (response) 
            real_ip = packet[ARP].psrc
            real_mac = packet[ARP].hwsrc

            # if IP already in dictionary, checking for MAC change
            if real_ip in ip_mac_mapping:
                if ip_mac_mapping[real_ip] != real_mac:
                    print(f"\n[ALERT] ARP SPOOFING DETECTED!")
                    print(f"IP Address: {real_ip}")
                    print(f"Original MAC: {ip_mac_mapping[real_ip]}")
                    print(f"Suspicious New MAC: {real_mac}\n")

            else:
                # new IP, saving the mapping
                ip_mac_mapping[real_ip] = real_mac
                print(f"[INFO] Learned mapping: {real_ip} -> {real_mac}")

def main():
    print("--- STARTING ARP SPOOF DETECTOR ---")
    print("Listening for ARP traffic on the local network...")
    print("Press Ctrl+C to stop at any time. \n")

    # sniffing network packets
    # filtering strictly for ARP traffic
    
    sniff(filter="arp", prn=process_packet, store=False) #store=False prevents memory bloat over long runs

if __name__ == "__main__":
    main()