# CTF Project Summary

## Project Overview

This repository contains a structured Capture The Flag (CTF) project setup designed to facilitate cybersecurity research, vulnerability testing, and CTF challenge participation. The project provides a comprehensive set of tools, resources, and documentation to support various aspects of cybersecurity investigations.

## What Was Accomplished

1. **Project Structure**: Established a well-organized directory structure with clear separation of tools, resources, writeups, and notes
2. **Dependency Management**: Created a comprehensive `requirements.txt` file with 114 dependencies organized by category
3. **OSINT Tool**: Developed `osint-checker.py` - a Python script for basic OSINT checks including WHOIS lookups, Shodan searches, and social media verification
4. **Documentation**: Created detailed documentation for tools, including usage examples and requirements
5. **Templates**: Provided a writeup template for documenting CTF challenge solutions
6. **Environment Setup**: Configured a Python virtual environment with essential tools pre-installed

## Key Findings About the CTF Event

- The project is focused on Open Source Intelligence (OSINT) gathering as a core capability
- It includes resources for a specific OSINT challenge related to "investigaosint-login.html"
- The tools and dependencies cover multiple CTF categories:
  - OSINT (python-whois, Shodan, social media checks)
  - Network exploitation (scapy, pwntools)
  - Cryptography (cryptography, pycryptodome)
  - Reverse engineering (capstone, keystone, unicorn)
  - Forensics (volatility3, pytsk3)
  - Web application testing (sqlmap, bs4, selenium)

## Platform Information

- **Operating System**: macOS (Darwin)
- **Python Version**: Python 3.14 (virtual environment available in `tools/venv/`)
- **Project Location**: `/Users/statick/apps/ctf/`
- **Git Repository**: Initialized git repository with .gitignore file

## Project Structure Overview

```
/Users/statick/apps/ctf/
├── requirements.txt          # Comprehensive list of Python dependencies
├── tools/                    # CTF tools and scripts
│   ├── osint-checker.py      # OSINT automation script
│   ├── README.md             # Tools documentation
│   ├── requirements.txt      # Tools-specific dependencies
│   └── venv/                 # Python virtual environment (Python 3.14)
├── resources/                # CTF challenge resources
│   └── investigaosint-login.html  # OSINT challenge resource
├── writeups/                 # Challenge writeups
│   └── writeup-template.md   # Template for documenting solutions
├── notes/                    # Research and investigation notes
└── .gitignore                # Git ignore configuration
```

## Tools Available

### Primary Tools

1. **osint-checker.py** - OSINT automation tool
   - WHOIS lookup for domain registration information
   - Shodan search for device and service information
   - Social media username verification across 6 platforms
   - Command-line interface with multiple options

### Dependencies (by category)

- **OSINT Tools**: python-whois, shodan, requests, beautifulsoup4, scrapy, selenium
- **Network Exploitation**: scapy, pwntools, requests-toolbelt
- **Cryptography**: cryptography, pycryptodome, pyopenssl, pyjwt
- **Reverse Engineering**: capstone, keystone-engine, unicorn, pefile, pyelftools, angr
- **Forensics**: volatility3, pytsk3, pillow, exifread, pdfminer.six, olefile
- **Web Application Testing**: sqlmapapi, flask, django, werkzeug
- **Programming**: numpy, pandas, matplotlib, jupyter

## Next Steps

1. **Expand Toolset**: Add more specialized tools for specific CTF categories
2. **Challenge Documentation**: Complete writeups for the investigaosint challenge
3. **Tool Enhancements**: Improve osint-checker.py with additional OSINT sources and features
4. **Environment Setup**: Create Docker containers for consistent tool execution
5. **Training Materials**: Develop tutorials and examples for using the tools
6. **Vulnerability Database**: Maintain a database of known vulnerabilities and exploits
7. **Collaboration**: Set up version control workflows for team collaboration
8. **Automation**: Create scripts to automate common CTF tasks and workflows

## Usage Examples

### osint-checker.py Basic Usage

```bash
# WHOIS lookup
python tools/osint-checker.py --whois example.com

# Shodan search (requires API key)
python tools/osint-checker.py --shodan 8.8.8.8 --shodan-api YOUR_API_KEY

# Social media check
python tools/osint-checker.py --social username

# Combine multiple checks
python tools/osint-checker.py --whois example.com --shodan 8.8.8.8 --shodan-api YOUR_API_KEY --social username
```

### Virtual Environment Setup

```bash
# Activate virtual environment
source tools/venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Notes

- This project is actively maintained and updated
- Tools and resources are periodically reviewed for relevance and effectiveness
- Always ensure compliance with applicable laws and ethical guidelines when using these tools
