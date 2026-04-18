
# 🐱 lazycat

A lazy way to manage your Docker Compose stacks from the terminal.

## What it does

- Lists all running containers grouped by their Compose stack
- Displays name, status, and image for each container

## Requirements

- Python 3.8+
- Docker running on your machine

## Installation

```bash
git clone https://github.com/yourusername/lazycat.git
cd lazycat
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Roadmap

- [x] List containers grouped by compose stack
- [ ] CLI commands — `ps`, `up`, `down`, `restart`
- [ ] Realtime log streaming
- [ ] TUI interface with keyboard navigation

---

*"Just a hobby, won't be big and professional" — Linus Torvalds, 1991*