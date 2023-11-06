#!/bin/bash

log_directory="/var/log"

found_files=$(grep -l "error" "$log_directory"/* 2>/dev/null)

if [ -n "$found_files" ]; then
    echo "the files with 'error' in  $log_directory:"
    echo "$found_files"
else
    echo "files with 'error' not found in $log_directory."
fi
