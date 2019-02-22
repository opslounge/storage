#!/bin/bash
for hba_devices in $(ls /sys/class/fc_host/); do
       port_name=$(cat /sys/class/fc_host/${hba_devices}/port_name | sed  's ..  ')
       echo -e "${port_name}"
done
