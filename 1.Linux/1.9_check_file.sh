#!/bin/bash

read -p "enter the name of file: " filename

if [ -e "$filename" ]; then
    cat "$filename"
else
    echo "error: file '$filename' does not exist!"
fi
