import os
import hashlib
import json

BASELINE_FILE = "baseline.json"
TARGET_DIR = "." # monitors current folder

def calculate_file_hash(filepath):
    """Calculates SHA-256 hash of a given file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            # reading file in chunks to handle large files efficiently
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def create_baseline():
    """Scans directory and saves file paths and hashes to baseline.json."""
    baseline = {}
    for root, dirs, files in os.walk(TARGET_DIR):
        for filename in files:
            # skips the baseline file and python script
            if filename in [BASELINE_FILE, "fim.py"]:
                continue

            filepath = os.path.join(root, filename)
            file_hash = calculate_file_hash(filepath)
            if file_hash:
                baseline[filepath] = file_hash

    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=4)
    print("[SUCCESS] Baseline snapshot created successfully!")

def check_integrity():
    """Compares files against saved baseline."""
    if not os.path.exists(BASELINE_FILE):
        print("[ERROR] No baseline found! Run baseline creation first.")
        return

    # loading existing baseline
    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)

    current_files ={}
    for root, dirs, files in os.walk(TARGET_DIR):
        for filename in files:
            if filename in [BASELINE_FILE, "fim.py"]:
                continue
            filepath = os.path.join(root, filename)
            file_hash = calculate_file_hash(filepath)
            if file_hash:
                current_files[filepath] = file_hash

    # checking for changes, deletions, and additions
    print("\n--- FILE INTEGRITY MONITORING REPORT ---")
    changes_detected = False

    # checking for modified or deleted files
    for path, old_hash in baseline.items():
        if path not in current_files:
            print(f"[ALERT] DELETED FILE: {path}")
            changes_detected = True

        elif current_files[path] != old_hash:
            print(f"[ALERT] MODIFIED FILE: {path} (Hash mismatch!)")
            changes_detected = True

    # checking for newly added files
    for path in current_files:
        if path not in baseline:
            print(f"[ALERT] NEW FILE ADDED: {path}")
            changes_detected = True

    if not changes_detected:
        print("[SECURE] No changes detected. All files match baseline.")


# --- simple menu interface ---
if __name__ == "__main__":
    choice = input("Do you want to (1) Create Baseline or (2) Check Intergrity? Enter 1 or 2:")
    if choice == "1":
        create_baseline()
    elif choice == "2":
        check_integrity()
    else:
        print("Invalid Choice. Run the script again.")