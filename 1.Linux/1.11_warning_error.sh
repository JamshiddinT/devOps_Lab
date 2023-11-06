#!/bin/bash

read -p "Enter the name of file: " file_name

if [ -e "$file_name" ]; then
    sed -i 's/error/warning/g' "$file_name"
    echo "'error' changed to 'warning' in  \"$file_name\"."
else
    echo "file \"$file_name\" does not exist."
fi
