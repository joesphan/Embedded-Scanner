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

## How it works

`Scan.py ` runs everything. The arguments are as follow:

`Scan.py -a`	Starts a new consecutive scan if one is not running, else scans the next image

`Scan.py -f`  Finishes the current consecutive scan. Runs `ConvertPdf.py` and `SendEmail.py` according to settings defined in profiles.conf

