# Windows System Monitoring and Threat Detection

A Python-based tool designed to monitor system activity, check browser settings, track network usage, and identify file modifications. It can be used for security analysis and investigation of potential malicious or suspicious activity on a Windows machine.

## Features

### 1. Browser Homepage Check
- Identifies the homepage settings for:
  - **Google Chrome**
  - **Mozilla Firefox**
  - **Internet Explorer**
- Helps detect unauthorized changes that may indicate a browser hijacking attempt.

### 2. Network Activity Monitoring
- Monitors outgoing and incoming network traffic using `psutil`.
- Alerts when data transfer exceeds a specified threshold (default: 1MB in 10 seconds).

### 3. Chrome Extension Inspection
- Retrieves and displays installed Chrome extensions with their names and versions by reading `manifest.json` files.

### 4. Firefox Add-on Inspection
- Identifies installed Firefox add-ons by reading the `extensions.json` file in Firefox profiles.

### 5. Suspicious File Scanner
- Scans specified directories for files modified within the last 24 hours.
- Generates a detailed report of these files for further investigation.

### 6. Windows Event Log Analysis
- Retrieves critical system events from the Windows Event Log, including:
  - System shutdowns
  - Unexpected shutdowns
  - Logon events
  - Policy changes
  - Process creation and termination
- Focuses on key event IDs such as `6006`, `6008`, `4624`.

## Installation
1. Clone the repository:
   ```bash
   https://github.com/William2716057/activityDetect.git
   cd /activityDetector
   ```
2. Install required dependencies:
   ```bash
   pip install psutil pywin32
   ```

## Usage
Run the script with:
```bash
python monitor.py
```

### Recommended Directories for File Scanning
Add the following directories to `directories_to_scan` for enhanced monitoring:
- `C:\Windows\System32`
- `C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default`
- `C:\Users\<username>\AppData\Roaming\Mozilla\Firefox\Profiles`

## Sample Output
```
Chrome homepage is set to: https://example.com
Bytes sent in last ten seconds: 2048
Warning: Unusual network activity detected!
Extension: AdBlock, Version: 5.1.0
Addon: uBlock Origin, Version: 1.47.3
Recently modified files: C:\Users\User\AppData\Local\Google\Chrome\User Data\Default\example.dll
TimeGenerated: 2025-03-20 14:12:45, EventID: 4624
```

## Security Recommendations
- Regularly review homepage settings and browser extensions.
- Investigate unusual network spikes.
- Cross-check modified files for suspicious behavior.
- Review Windows Event Logs for unexpected logon attempts or shutdowns.

## Disclaimer
This tool is intended for legitimate security monitoring and educational purposes only. Use it responsibly.


