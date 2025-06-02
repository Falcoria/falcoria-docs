# Falcoria CLI – Installation Guide

Falcoria CLI (`falcli`) is the command-line interface for configuring and managing distributed scans through the Falcoria platform. This guide covers installation and setup of the CLI tool only.

> **Note:**  
> The CLI requires a running Falcoria backend (ScanLedger, Tasker, Redis, RabbitMQ).  
> This guide does not include backend deployment steps.

---

## Requirements

- Python 3.8 or higher
- Git
- Linux or macOS (Windows is supported via WSL or Python virtualenv)

---

## Installation Steps

```bash
# Clone the repository
git clone https://github.com/Falcoria/falcli.git
cd falcli

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python3 falcli.py
```

---

## CLI Overview

```bash
Usage: falcli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --version, -v             Show the version and exit.
  --install-completion      Install shell completion.
  --show-completion         Show shell completion info.
  --help                    Show this message and exit.

Commands:
  fast-scan   Start a quick scan, track it, and download report
  project     Manage projects and IP data.
  config      Configure CLI settings and backend URLs.
  memory      View or clear stored memory state.
  scan        Start, stop, or preview scans.
  workers     Manage worker nodes and their IPs.
```
