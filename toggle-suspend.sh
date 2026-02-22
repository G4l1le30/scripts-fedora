#!/bin/bash

export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u)/bus

LOG_FILE="$HOME/toggle-suspend.log"
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

echo "[$TIMESTAMP] Running toggle-suspend.sh" >> "$LOG_FILE" 2>&1

DAY=$(date +%u)

if [ "$DAY" -ge 1 ] && [ "$DAY" -le 5 ]; then
    # Weekday → Disable suspend when plugged in
    echo "[$TIMESTAMP] It's a weekday. Disabling suspend on AC power." >> "$LOG_FILE" 2>&1
    gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'nothing' >> "$LOG_FILE" 2>&1
    echo "[$TIMESTAMP] Current sleep-inactive-ac-type: $(gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type)" >> "$LOG_FILE" 2>&1
else
    # Weekend → Enable suspend after 2 hours
    echo "[$TIMESTAMP] It's a weekend. Enabling suspend on AC power after 2 hours." >> "$LOG_FILE" 2>&1
    gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'suspend' >> "$LOG_FILE" 2>&1
    gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout 7200 >> "$LOG_FILE" 2>&1
    echo "[$TIMESTAMP] Current sleep-inactive-ac-type: $(gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type)" >> "$LOG_FILE" 2>&1
    echo "[$TIMESTAMP] Current sleep-inactive-ac-timeout: $(gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout)" >> "$LOG_FILE" 2>&1
fi
echo "[$TIMESTAMP] toggle-suspend.sh finished." >> "$LOG_FILE" 2>&1
