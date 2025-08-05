import json
from colorama import Fore, Style

with open('data/storage-accounts.json') as f:
    storage_accounts = json.load(f)

def check_misconfigs(account):
    misconfigs = []
    if account.get("allowBlobPublicAccess", False):
        misconfigs.append("Public blob access enabled")
    if not account.get("supportsHttpsTrafficOnly", True):
        misconfigs.append("Unencrypted traffic allowed (HTTP enabled)")
    if account.get("minimumTlsVersion", "TLS1_2") != "TLS1_2":
        misconfigs.append(f"Insecure TLS version: {account['minimumTlsVersion']}")
    return misconfigs

print(f"\n{Fore.CYAN}🔍 STORAGE MISCONFIGURATION SCAN RESULTS{Style.RESET_ALL}\n")

for acct in storage_accounts:
    issues = check_misconfigs(acct)
    if issues:
        print(f"{Fore.RED}❌ {acct['name']} ({acct['location']}){Style.RESET_ALL}")
        for i in issues:
            print(f"   - {i}")
    else:
        print(f"{Fore.GREEN}✅ {acct['name']} is compliant{Style.RESET_ALL}")
