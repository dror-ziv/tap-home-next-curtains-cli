# TapHome curtain CLI tool
This is a simple CLI tool for controlling TapHome curtains.

## Installation
```bash
pip install -r requirements.txt
```
* fill config.yaml file with your credentials
* run `main.py setup`

### recommended
* add `alias up="python3 /path/to/main.py up"` to your .bashrc or .zshrc file

## Usage
```bash
python3 main.py up
python3 main.py down
python3 main.py setup
```

## commands
* `up` - open all curtains that are configured in config.yaml
* `down` - close all curtains that are configured in config.yaml
* `setup` - setup curtains, required before first use and after adding new curtains to config.yaml