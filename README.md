# TapHome curtain CLI tool
This is a simple CLI tool for controlling TapHome curtains.

## Installation
```bash
pip install -r requirements.txt
```
* fill config.yaml file with your credentials
* run `cli.py setup`

### recommended
* add `alias up="python3 /path/to/cli.py up"` to your .bashrc or .zshrc file

## Usage
```bash
python3 cli.py up
python3 cli.py down
python3 cli.py setup
```

## commands
* `up` - open all curtains that are configured in config.yaml
* `down` - close all curtains that are configured in config.yaml
* `setup` - setup curtains, required before first use and after adding new curtains to config.yaml