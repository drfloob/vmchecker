#!/bin/bash

rm qr.png; 
echo "checker.py" > tmp && cat check.py >> tmp && qrencode -o qr.png < tmp && feh qr.png 
