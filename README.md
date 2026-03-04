# CTF Project

This project is a collection of tools, resources, and templates for Capture The Flag (CTF) challenges and cybersecurity research.

## Project Structure

### `/tools/`
Contains various tools and scripts designed to assist with CTF challenges and cybersecurity research. Currently includes:
- `osint-checker.py`: A Python script for basic OSINT checks (WHOIS, Shodan, social media)
- `README.md`: Detailed documentation for all tools
- `requirements.txt`: Tools-specific dependencies

### `/writeups/`
Directory for storing challenge writeups. Use this to document your solutions to CTF challenges.

### `/notes/`
Directory for storing CTF-related notes. Use this for taking notes during challenges or research.

### `/resources/`
Directory for storing CTF resources. Use this for reference materials, cheat sheets, or other helpful resources.

## Requirements

The project has two requirements files:

1. `/requirements.txt`: Comprehensive project requirements organized by category (OSINT, network exploitation, cryptography, etc.)
2. `/tools/requirements.txt`: Tools-specific dependencies (required for osint-checker.py)

## Virtual Environment

A virtual environment with all dependencies installed is available in `/tools/venv/`. To activate it:

```bash
# On macOS/Linux
source tools/venv/bin/activate

# On Windows
.\tools\venv\Scripts\activate
```

## Usage

### OSINT Checker Tool

The `osint-checker.py` tool can perform various OSINT checks. See `/tools/README.md` for detailed usage instructions.

## Linting

This project uses Ruff for linting. To run linting:

```bash
ruff check .
```

## Contributing

- Add new tools to the `/tools/` directory
- Document all tools in `/tools/README.md`
- Store writeups in `/writeups/`
- Store notes in `/notes/`
- Store resources in `/resources/`

## License

MIT License