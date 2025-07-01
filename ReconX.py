import whois
import dns.resolver
import requests
import json
import sys
import re
from urllib.parse import urlparse

def clean_domain(input_str):
    parsed = urlparse(input_str)
    domain = parsed.netloc if parsed.netloc else parsed.path
    return domain.lstrip("www.")

def is_valid_domain(domain):
    pattern = re.compile(
        r"^(?!\-)(?:[a-zA-Z0-9\-]{0,62}[a-zA-Z0-9]\.)+[a-zA-Z]{2,}$"
    )
    return bool(pattern.match(domain))

def print_section(title):
    print(f"\n\033[94m[{title}]\033[0m")

def whois_lookup(domain):
    print_section(f"WHOIS Lookup for {domain}")
    try:
        w = whois.whois(domain)
        print(json.dumps(w, indent=2, default=str))
    except Exception as e:
        print(f"\033[91mError WHOIS: {e}\033[0m")

def dns_lookup(domain):
    print_section(f"DNS Records for {domain}")
    record_types = ['A', 'AAAA', 'NS', 'MX', 'TXT', 'CNAME']
    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            print(f"\n{rtype} Records:")
            for r in answers:
                print(f" - {r.to_text()}")
        except dns.resolver.NoAnswer:
            print(f" - No {rtype} record found.")
        except dns.resolver.NXDOMAIN:
            print(f" - {rtype}: Domain does not exist.")
        except Exception as e:
            print(f" - {rtype} Error: {e}")

def crtsh_subdomains(domain):
    print_section(f"crt.sh Subdomain Enumeration for {domain}")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    headers = {
        "User-Agent": "ReconX/1.0"
    }
    try:
        resp = requests.get(url, headers=headers, timeout=30)
        if resp.status_code == 200:
            data = resp.json()
            subdomains = set(entry['name_value'] for entry in data)
            for sub in sorted(subdomains):
                print(f" - {sub}")
        else:
            print(f" - Failed to retrieve data (Status code: {resp.status_code})")
    except requests.exceptions.Timeout:
        print(f" - Timeout: crt.sh took too long to respond.")
    except Exception as e:
        print(f" - Error: {e}")

def shodan_and_censys_links(domain):
    print_section("External Recon Services")
    print(f" - Shodan: https://www.shodan.io/search?query={domain}")
    print(f" - Censys: https://search.censys.io/domain/{domain}")

def run_recon(domain):
    whois_lookup(domain)
    dns_lookup(domain)
    crtsh_subdomains(domain)
    shodan_and_censys_links(domain)

def main():
    if len(sys.argv) != 2:
        print("Uso: python ReconX.py <dominio o URL>")
        sys.exit(1)

    raw_input = sys.argv[1]
    domain = clean_domain(raw_input)

    if not is_valid_domain(domain):
        print(f"\033[91m[!] Dominio no válido: {domain}\033[0m")
        sys.exit(1)

    run_recon(domain)

if __name__ == "__main__":
    main()
