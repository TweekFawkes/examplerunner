import sys
import argparse
from urllib.parse import urlparse
import socket

def extract_domain_and_port(input_str):
    # Parse URL if given a full URL
    parsed = urlparse(input_str if '://' in input_str else f'http://{input_str}')
    domain = parsed.netloc or parsed.path
    
    # Split domain and port if port exists
    if ':' in domain:
        domain, port = domain.split(':')
        port = int(port)
    else:
        port = None
        
    return domain.strip('/'), port

def resolve_domain(domain):
    try:
        # Get all IP addresses associated with the domain
        ip_addresses = socket.getaddrinfo(domain, None)
        # Extract unique IP addresses (removing duplicates and considering only IPv4 and IPv6)
        unique_ips = set(addr[4][0] for addr in ip_addresses)
        return list(unique_ips)
    except socket.gaierror:
        return []

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--domain_name', required=True, help='Domain name to check')
    args = parser.parse_args()

    domain, port = extract_domain_and_port(args.domain_name)
    print(f"\n[*] Checking domain: {domain}")

    # Resolve IP addresses
    ip_addresses = resolve_domain(domain)
    if ip_addresses:
        print("\n[*] Resolved IP addresses:")
        for ip in ip_addresses:
            print(f"    - {ip}")
    else:
        print("\n[!] Could not resolve any IP addresses")

if __name__ == "__main__":
    main()
