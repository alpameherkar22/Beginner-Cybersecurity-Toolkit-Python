import re
import csv
import json

# setting up thresold and tracking stucture
THRESHOLD = 3
failed_ips = {}

# defining regex pattern to find ip address
ip_pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

# reading log file
with open("auth.log", "r") as file:
    for line in file:
        if "Failed Password" in line: # checking failed password attempt
            match = re.search(ip_pattern, line) # searching ip address in line
            if match:
                ip = match.group(1) # extracting matched ip string

# updating count in dictionary
                if ip in failed_ips:
                    failed_ips[ip] += 1
                else:
                    failed_ips[ip] = 1

# printing alerts for IPs exceeding threshold
# filtering alerts and display in console 
alerts = []
print("--- SECURITY LOG ANALYSIS REPORT ---")
for ip, count in failed_ips.items():
    if count >= THRESHOLD:
        print(f"[ALERT] Potential Brute Force Attack detected from IP: {ip} ({count} failed attempts)")
        # saving each alert as a dictionary for structure export
        alerts.append({
            "ip_address": ip,
            "failed_attempts": count
        })

# exporting alerts to csv
with open("alerts.csv", "w", newline="") as csv_file:
    fieldnames = ["ip_address", "failed_attempts"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader() #column headers
    writer.writerows(alerts) #alerts in rows

# exporting alerts to json
with open("alerts.json", "w") as json_file:
    json.dump(alerts, json_file, indent=4) #indent for readable spacing

print("\n[SUCCESS] Reports exported to 'alerts.csv' and'alerts.json'.")