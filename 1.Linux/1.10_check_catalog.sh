#!/bin/bash

read -p "enter the name of catalog: " directory_name

if [ -d "$directory_name" ]; then    
    echo "list of the files in \"$directory_name\":"
    ls "$directory_name"
else
    echo "Catalog \"$directory_name\" does not exist."
fi
