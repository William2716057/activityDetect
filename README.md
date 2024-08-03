# Browser Security and Network Monitoring Script

A Python script that provides functionalities to monitor browser homepages, network activity, browser extensions, and suspicious file modifications on a Windows system. 
The script includes features to check browser settings in the registry, monitor network data, list installed Chrome extensions and Firefox add-ons, and scan specified directories for suspicious files.

## Features
1. Check Browser Homepage:
- Inspects the homepage settings for Chrome, Firefox, and Internet Explorer from the Windows registry.

2. Monitor Network Activity:
- Monitors network data sent and received every 10 seconds and alerts if the data exceeds a specified threshold.

3. Check Chrome Extensions:
- Lists all installed Chrome extensions with their names and versions by reading the manifest.json files.

4. Check Firefox Add-ons:
- Lists all installed Firefox add-ons with their names and versions by reading the extensions.json files in each Firefox profile.

5. Scan for Suspicious Files:
- Scans specified directories for files modified within the last 24 hours and logs their paths.
