# DESCRIPTION

Bulk add terminal server agents to NGFW or PANORAMA using CLI (scripting)

# TESTED
Tested on PanOS version: 8.0.3, 10.0.0

### STEP 1

Run the script and it will generate a config file in current directory.
Example: ./main.py myconfig.txt myhost-01.network.com 

### STEP 2

SSH to firewall.
Example: ssh admin@pa.company.net

### STEP 3

Paste config. (commit is added to the end. You might want to verify config in GUI before commit)

# LIMITATIONS / IMPROVEMENTS
Script is not dynamic in regards to FQDN delimiters. You must edit script manually.

