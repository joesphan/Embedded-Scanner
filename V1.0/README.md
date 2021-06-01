# Embedded-Scanner
Turn a regular usb printer/scanner into a email/nas scanner
Need:
- raspberry pi/embedded device running linux
- usb printer/scanner
- buttons

## Goals
- Use simple HW buttons for scanning and emailing
- Make it easy to reconnect to internet if Wi-Fi drops
- Headless device



## Installation

CD to the downloaded folder

run:

```sh
sudo apt-get install sane sane-utils libsane-extras units python python-smbus i2c-tools 
```

```python 
python setup.py
```

```python
pip install Pillow
```



## Settings
read `/Docs/profiles documentation.txt`

settings can be set via the web UI

## GPIO Setup

This script is designed to work on both the raspberry pi and the now defunct ntc CHIP platform. Hook up 6 buttons to your device and name them according to [CHIP-IO](https://pypi.org/project/CHIP-IO/) naming conventions or [RPI.GPIO](https://pypi.org/project/RPi.GPIO/) naming conventions.

## How it works

CHIP_GPIO or RPI_GPIO will monitor buttons and call scan.py

`Scan.py ` runs everything. The arguments are as follow:

`Scan.py -a`	Starts a new consecutive scan if one is not running, else scans the next image

`Scan.py -f`  Finishes the current consecutive scan. Runs `ConvertPdf.py` and `SendEmail.py` according to settings defined in profiles.conf

## Web UI

## Credits

Backend: Joesphan Lu, copyright @ 2020 Ok for non-commercial use. Redistribution prohibited

Web UI: Lucas Zhou (hopefully) @ 2020