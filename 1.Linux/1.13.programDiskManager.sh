#!/bin/bash

# function to diplay disk info
display_disk_space() {
    df -h
}

# function for sending notification
send_warning() {
    local disk="$1"
    local threshold="$2"
    local free_space=$(df -k "$disk" | awk 'NR==2 {print $4}')
    
    if [ "$free_space" -lt "$threshold" ]; then
        echo "warning: free space of disk $disk decreasing to ($threshold KB)." >> disk_manager.log
    fi
}

# function for clean disk
clean_disk() {
    local disk="$1"
    # add here real logic
    echo "cleaned in the disk $disk." >> disk_manager.log
}

# function for logging
log_event() {
    local message="$1"
    echo "$(date): $message" >> disk_manager.log
}

# main cycle working with arguments
while [ $# -gt 0 ]; do
    case "$1" in
        -s|--stat)
            display_disk_space
            ;;
        -w|--warning)
            shift
            disk="$1"
            shift
            threshold="$1"
            send_warning "$disk" "$threshold"
            ;;
        -c|--clean)
            shift
            disk="$1"
            clean_disk "$disk"
            ;;
        *)
            echo "wrong argument: $1"
            ;;
    esac
    shift
done

# ./disk_manager.sh -s  # Отобразить статистику
# ./disk_manager.sh -w /dev/sda 1024  # Отправить предупреждение для диска /dev/sda
# ./disk_manager.sh -c /dev/sdb  # Очистить диск /dev/sdb
