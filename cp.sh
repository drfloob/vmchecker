#!/bin/bash

while [ 1 ];
do
    mount /media/removable
    SUCC=$?
    if [ $SUCC -eq "0" ]; then
	# success
	break;
    fi
    sleep 1;
done

cp check.py /media/removable/sl4a/scripts/mine/
umount /media/removable

echo "DONE"