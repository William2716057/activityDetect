import winreg
import psutil
import time
import os
import json

def check_browser_homepage(): #adjust
    browsers = {
        "Chrome": r"Software\Policies\Google\Chrome",
        "Firefox": r"Software\Policies\Mozilla\Firefox",
        "IE": r"Software\Microsoft\Internet Explorer\Main"
    }
    
    for browser, path in browsers.items():
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_READ)
            homepage, _ = winreg.QueryValueEx(registry_key, "Start Page")
            print(f"{browser} homepage is set to: {homepage}")
            winreg.CloseKey(registry_key)
        except FileNotFoundError:
            print(f"{browser} settings not found in the registry.")
        except Exception as e:
            print(f"An error occurred while checking {browser} settings: {e}")

check_browser_homepage()

def monitor_network_activity(threshold=1024*1024):
    print("Monitoring network activity...")
    old_data = psutil.net_io_counters()
    time.sleep(10)  # Monitor every 10 seconds
    new_data = psutil.net_io_counters()

    sent = new_data.bytes_sent - old_data.bytes_sent
    recv = new_data.bytes_recv - old_data.bytes_recv

    print(f"Bytes sent in last ten seconds: {sent}")
    print(f"Bytes received in last ten seconds: {recv}")

    if sent > threshold or recv > threshold:
        print("Warning: Unusual network activity detected!")

monitor_network_activity()

def check_chrome_extensions():
    chrome_extensions_path = os.path.expanduser('~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions') #adjust
    
    if not os.path.exists(chrome_extensions_path):
        print("Chrome extensions path not found.")
        return

    for extension in os.listdir(chrome_extensions_path):
        manifest_path = os.path.join(chrome_extensions_path, extension, 'manifest.json')
        if os.path.exists(manifest_path):
            with open(manifest_path, 'r') as file:
                manifest = json.load(file)
                print(f"Extension: {manifest.get('name', 'Unknown')}, Version: {manifest.get('version', 'Unknown')}")
        else:
            print(f"Manifest file not found for extension: {extension}")

check_chrome_extensions()

def check_firefox_addons():
    firefox_profile_path = os.path.expanduser('~\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles') #adjust
    
    if not os.path.exists(firefox_profile_path):
        print("Firefox profile path not found.")
        return
    
    for profile in os.listdir(firefox_profile_path):
        addons_path = os.path.join(firefox_profile_path, profile, 'extensions.json')
        if os.path.exists(addons_path):
            with open(addons_path, 'r') as file:
                addons = json.load(file)
                for addon in addons.get('addons', []):
                    print(f"Addon: {addon.get('name', 'Unknown')}, Version: {addon.get('version', 'Unknown')}")
        else:
            print(f"Add-ons file not found for profile: {profile}")

check_firefox_addons()

def scan_for_suspicious_files(directories, threshold=24*60*60):
    current_time = time.time()
    results = []

    for directory in directories:
        if not os.path.exists(directory):
            message = f"Directory {directory} does not exist."
            print(message)
            results.append(message)
            continue

        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_stat = os.stat(file_path)
                
                # Check if the file was modified within the threshold
                if current_time - file_stat.st_mtime < threshold:
                    message = f"Suspicious file detected: {file_path}"
                    print(message)
                    results.append(message)

    with open("scan_results.txt", "w") as result_file:
        for result in results:
            result_file.write(result + "\n")

directories_to_scan = [
    os.path.expanduser('~\\AppData\\Local\\Google\\Chrome\\User Data\\Default'), # adjust
    os.path.expanduser('~\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles') # adjust
]

scan_for_suspicious_files(directories_to_scan)