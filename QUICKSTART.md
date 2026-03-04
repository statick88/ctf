# CTF Project Quick Start Guide

## 1. Environment Setup

### Prerequisites
- Python 3.9+ installed
- Git configured

### Setup Steps
1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd ctf
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   # or
   venv\Scripts\activate    # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 2. Using osint-checker.py Tool

### What is osint-checker.py?
A tool for checking email addresses and phone numbers against multiple OSINT services.

### Basic Usage
```bash
cd tools
python3 osint-checker.py
```

### Available Commands
- `email <email>` - Check email addresses
- `phone <phone>` - Check phone numbers
- `help` - Show available commands
- `exit` - Quit the tool

### Example
```bash
osint-checker> email test@example.com
osint-checker> phone +1234567890
```

## 3. Documenting Challenges and Writeups

### Challenge Documentation
- Challenges are typically stored in the `notes/` directory
- Create a separate file for each challenge
- Include:
  - Challenge name and category
  - Description
  - Hints (if available)
  - Solution approach
  - Flag

### Writeups
- Writeups are stored in the `writeups/` directory
- Use Markdown format (`.md`) for easy reading
- Structure:
  1. Challenge description
  2. Approach and methodology
  3. Step-by-step solution
  4. Flag
  5. Lessons learned

## 4. Key Information Locations

### Project Structure
```
ctf/
├── notes/               # Challenge documentation
├── resources/           # Reference materials (wordlists, tools, etc.)
├── tools/               # Custom scripts and tools
│   ├── osint-checker.py  # OSINT verification tool
│   └── venv/            # Virtual environment
└── writeups/            # Challenge solutions and writeups
```

### Useful Files
- `requirements.txt` - Project dependencies
- `tools/README.md` - Detailed tool documentation
- `resources/` - Contains wordlists, reference guides, and other assets

## 5. Additional Tips

- Always activate the virtual environment before running tools
- Keep documentation up to date
- Use the `help` command within osint-checker.py for detailed usage info
- Check `resources/` for pre-built wordlists and reference materials