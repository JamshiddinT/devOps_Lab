#!/bin/bash

if [ $EUID -eq 0 ]; then
	echo "Script initialized by root user."
else
	echo "script not initialized by root user."
fi 
