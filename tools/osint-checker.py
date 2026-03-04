#!/usr/bin/env python3
"""
OSINT Checker - A simple Python script for basic OSINT checks
Author: Giga Potato
Date: 2026-03-03
Version: 1.0

This script provides functions for basic OSINT checks including:
- WHOIS lookup
- Shodan search
- Social media checks
- Command-line interface

Requirements:
- python-whois
- shodan
- argparse
- requests
"""

import argparse
import sys
import whois
import shodan
import requests
from typing import Optional, Dict, List


def check_whois(domain: str) -> Optional[Dict]:
    """
    Perform WHOIS lookup on a domain.

    Args:
        domain: Domain name to check

    Returns:
        Dictionary with WHOIS information or None if lookup fails
    """
    try:
        print(f"[+] Performing WHOIS lookup for {domain}")
        w = whois.whois(domain)

        # Extract relevant information
        whois_info = {
            "domain_name": w.domain_name,
            "registrar": w.registrar,
            "creation_date": w.creation_date,
            "expiration_date": w.expiration_date,
            "last_updated": w.last_updated,
            "name_servers": w.name_servers,
            "emails": w.emails,
            "registrant_country": w.registrant_country,
        }

        return whois_info

    except Exception as e:
        print(f"[-] WHOIS lookup failed: {e}")
        return None


def check_shodan(ip: str, api_key: str) -> Optional[Dict]:
    """
    Perform Shodan search on an IP address.

    Args:
        ip: IP address to check
        api_key: Shodan API key

    Returns:
        Dictionary with Shodan information or None if search fails
    """
    try:
        print(f"[+] Performing Shodan search for {ip}")
        api = shodan.Shodan(api_key)
        result = api.host(ip)

        # Extract relevant information
        shodan_info = {
            "ip": result["ip_str"],
            "org": result.get("org", "N/A"),
            "isp": result.get("isp", "N/A"),
            "country": result.get("country_name", "N/A"),
            "city": result.get("city", "N/A"),
            "ports": result.get("ports", []),
            "hostnames": result.get("hostnames", []),
            "os": result.get("os", "N/A"),
        }

        return shodan_info

    except shodan.APIError as e:
        print(f"[-] Shodan API error: {e}")
        return None
    except Exception as e:
        print(f"[-] Shodan search failed: {e}")
        return None


def check_social_media(username: str) -> List[Dict]:
    """
    Check social media platforms for a username.

    Args:
        username: Username to check

    Returns:
        List of dictionaries with platform information
    """
    platforms = [
        {"name": "GitHub", "url": f"https://github.com/{username}"},
        {"name": "Twitter", "url": f"https://twitter.com/{username}"},
        {"name": "LinkedIn", "url": f"https://linkedin.com/in/{username}"},
        {"name": "Instagram", "url": f"https://instagram.com/{username}"},
        {"name": "Facebook", "url": f"https://facebook.com/{username}"},
        {"name": "Reddit", "url": f"https://reddit.com/user/{username}"},
    ]

    results = []

    print(f"[+] Checking social media platforms for username: {username}")

    for platform in platforms:
        try:
            response = requests.get(platform["url"], timeout=5)

            status = "Found" if response.status_code == 200 else "Not Found"

            results.append(
                {
                    "platform": platform["name"],
                    "url": platform["url"],
                    "status": status,
                    "status_code": response.status_code,
                }
            )

        except requests.exceptions.RequestException as e:
            results.append(
                {
                    "platform": platform["name"],
                    "url": platform["url"],
                    "status": "Error",
                    "status_code": str(e),
                }
            )

    return results


def print_whois_info(info: Dict):
    """Print WHOIS information in a readable format."""
    if not info:
        return

    print("\n=== WHOIS Information ===")
    for key, value in info.items():
        print(f"{key.replace('_', ' ').title()}: {value}")


def print_shodan_info(info: Dict):
    """Print Shodan information in a readable format."""
    if not info:
        return

    print("\n=== Shodan Information ===")
    for key, value in info.items():
        print(f"{key.replace('_', ' ').title()}: {value}")


def print_social_media_info(info: List[Dict]):
    """Print social media information in a readable format."""
    if not info:
        return

    print("\n=== Social Media Checks ===")
    for platform in info:
        print(
            f"{platform['platform']:<10} | {platform['status']:<10} | {platform['url']}"
        )


def main():
    parser = argparse.ArgumentParser(
        description="OSINT Checker - A simple tool for basic OSINT checks",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python osint-checker.py --whois example.com
  python osint-checker.py --shodan 8.8.8.8 --shodan-api YOUR_API_KEY
  python osint-checker.py --social username
  python osint-checker.py --whois example.com --shodan 8.8.8.8 --shodan-api YOUR_API_KEY --social username

Required packages:
  pip install python-whois shodan requests
""",
    )

    parser.add_argument("--whois", help="Domain name to perform WHOIS lookup")
    parser.add_argument("--shodan", help="IP address to perform Shodan search")
    parser.add_argument("--shodan-api", help="Shodan API key")
    parser.add_argument("--social", help="Username to check on social media platforms")

    args = parser.parse_args()

    if not any([args.whois, args.shodan, args.social]):
        parser.print_help()
        sys.exit(1)

    if args.shodan and not args.shodan_api:
        print("[-] Shodan API key is required for Shodan search")
        parser.print_help()
        sys.exit(1)

    # Perform WHOIS lookup
    if args.whois:
        whois_info = check_whois(args.whois)
        print_whois_info(whois_info)

    # Perform Shodan search
    if args.shodan and args.shodan_api:
        shodan_info = check_shodan(args.shodan, args.shodan_api)
        print_shodan_info(shodan_info)

    # Check social media
    if args.social:
        social_info = check_social_media(args.social)
        print_social_media_info(social_info)

    print("\n[+] OSINT checks completed")


if __name__ == "__main__":
    main()
