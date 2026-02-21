#!/bin/bash

export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u)/bus

DAY=$(date +%u)

if [ "$DAY" -ge 1 ] && [ "$DAY" -le 5 ]; then
    # Weekday → Disable suspend when plugged in
    gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'nothing'
else
    # Weekend → Enable suspend after 2 hours
    gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'suspend'
    gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout 7200
fi
