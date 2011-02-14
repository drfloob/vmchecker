#!/bin/bash

rm qr.png; 
echo "vmchecker.py" > tmp && cat check.py >> tmp && qrencode -o qr.png < tmp && feh qr.png 
