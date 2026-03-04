# Tools Directory

This directory contains various tools and scripts designed to assist with Capture The Flag (CTF) challenges and cybersecurity research.

## Purpose

The tools here are focused on:
- Open Source Intelligence (OSINT) gathering
- Vulnerability scanning and exploitation
- Network analysis
- Cryptography and steganography
- Other CTF-related tasks

## Current Tools

### osint-checker.py

A simple Python script for basic OSINT checks.

#### Features

- **WHOIS Lookup**: Retrieve domain registration information
- **Shodan Search**: Search for device information on Shodan
- **Social Media Checks**: Verify username existence across popular platforms
- **Command-line interface**: Easy to use with various options

#### Requirements

```bash
pip install python-whois shodan requests
```

#### Usage

```bash
# WHOIS lookup
python osint-checker.py --whois example.com

# Shodan search (requires API key)
python osint-checker.py --shodan 8.8.8.8 --shodan-api YOUR_API_KEY

# Social media check
python osint-checker.py --social username

# Combine multiple checks
python osint-checker.py --whois example.com --shodan 8.8.8.8 --shodan-api YOUR_API_KEY --social username
```

#### Options

- `--whois`: Domain name to perform WHOIS lookup
- `--shodan`: IP address to perform Shodan search
- `--shodan-api`: Shodan API key (required for Shodan search)
- `--social`: Username to check on social media platforms

#### Example Output

```
[+] Performing WHOIS lookup for example.com

=== WHOIS Information ===
Domain Name: ['EXAMPLE.COM', 'example.com']
Registrar: RESERVED-Internet Assigned Numbers Authority
Creation Date: 1995-08-14 04:00:00
Expiration Date: 2024-08-13 04:00:00
Last Updated: 2023-08-14 07:01:30
Name Servers: ['A.IANA-SERVERS.NET', 'B.IANA-SERVERS.NET']
Emails: ['abuse@iana.org']
Registrant Country: US

[+] OSINT checks completed
```

## Adding New Tools

When adding new tools to this directory:
1. Ensure they are well-documented
2. Include usage examples
3. List any dependencies
4. Follow Python/scripting best practices
5. Keep tools focused on CTF/cybersecurity tasks

## Contributing

- Test tools before adding them
- Keep tools simple and focused
- Document any dependencies clearly
- Add examples of usage