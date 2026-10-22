import urllib.request
import urllib.error
import os

# targeting URL (Using safe, public testing web app)
TARGET_URL = "http://localhost:8000"
WORDLIST_FILE = "wordlist.txt"

def brute_force():
    if not os.path.exists(WORDLIST_FILE):
        print(f"[ERROR] Could not find {WORDLIST_FILE}")
        return

    print(f"--- STARTING BRUTE-FORCE ON: {TARGET_URL} ---")

    with open(WORDLIST_FILE, "r") as f:
        for line in f:
            directory = line.strip()

            # skipping empty lines or comments
            if not directory or directory.startswith("#"):
                continue

            url = f"{TARGET_URL}/{directory}"

            try:
                # attempting to open/request URL
                response = urllib.request.urlopen(url, timeout=2) # adding timeout so it moves on quickly if a site is dead
                status = response.getcode()

                if status == 200:
                    print(f"[FOUND - 200 OK] {url}")

            except urllib.error.HTTPError as e:
                # handling server errors like 404 (Not Found) or 403 (Forbidden)
                if e.code == 403:
                    print(f"[FORBIDDEN - 403] {url} (Protected area!)")
                # skipping 404 for now to test a clean terminal
            except urllib.error.URLError as e:
                print(f"[TIMEOUT/ERROR] Skipping {url} ({e.reason})")
                continue

if __name__ == "__main__":
    brute_force()