# CTF Project Quick Reference Card

## Key File Locations
| Path | Description |
|------|-------------|
| `/Users/statick/apps/ctf/` | Project root directory |
| `requirements.txt` | Comprehensive Python dependencies (114 packages) |
| `tools/` | CTF tools and scripts |
| `tools/osint-checker.py` | OSINT automation tool (WHOIS, Shodan, social media checks) |
| `tools/venv/` | Python 3.14 virtual environment |
| `tools/requirements.txt` | Tools-specific dependencies |
| `tools/README.md` | Detailed tool documentation |
| `resources/` | CTF challenge resources (including investigaosint-login.html) |
| `writeups/` | Challenge solutions and writeups |
| `writeups/writeup-template.md` | Template for documenting solutions |
| `notes/` | Research and investigation notes |
| `.gitignore` | Git ignore configuration |

## Important Commands
### Virtual Environment
```bash
# Activate virtual environment
source tools/venv/bin/activate  # macOS/Linux
.\tools\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Deactivate virtual environment
deactivate
```

### osint-checker.py Tool
```bash
# Basic usage
cd tools
python3 osint-checker.py

# Command-line interface
osint-checker> email <email>    # Check email addresses
osint-checker> phone <phone>    # Check phone numbers
osint-checker> help              # Show available commands
osint-checker> exit              # Quit the tool

# Direct command-line options
python tools/osint-checker.py --whois example.com
python tools/osint-checker.py --shodan 8.8.8.8 --shodan-api YOUR_API_KEY
python tools/osint-checker.py --social username
python tools/osint-checker.py --whois example.com --shodan 8.8.8.8 --shodan-api YOUR_API_KEY --social username
```

### Linting
```bash
# Run Ruff linting
ruff check .
```

### Git
```bash
# Check repository status
git status

# Add changes
git add .

# Commit changes
git commit -m "Your commit message"
```

## Platform URLs
N/A - This is a local CTF project setup

## Event Details
- **Project Focus**: Open Source Intelligence (OSINT) gathering and multi-category CTF challenges
- **Core Capabilities**:
  - OSINT (WHOIS, Shodan, social media checks)
  - Network exploitation (scapy, pwntools)
  - Cryptography (cryptography, pycryptodome)
  - Reverse engineering (capstone, keystone, unicorn)
  - Forensics (volatility3, pytsk3)
  - Web application testing (sqlmap, bs4, selenium)
- **Active Challenge**: investigaosint (OSINT challenge)
- **Environment**: macOS (Darwin) with Python 3.14 virtual environment

## Quick Tips
- Always activate the virtual environment before running tools
- Document challenges in `notes/` and solutions in `writeups/`
- Use Markdown format for writeups
- Check `resources/` for wordlists and reference materials
- Keep documentation up to date
