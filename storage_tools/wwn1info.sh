#!/bin/bash

for hba_devices in $(ls /sys/class/fc_host/); do
       model=$(awk '{print $1, $2}' /sys/class/fc_host/${hba_devices}/symbolic_name)
       firmware_version=$(awk '{print $3}' /sys/class/fc_host/${hba_devices}/symbolic_name)
       driver_version=$(awk '{print $4}' /sys/class/fc_host/${hba_devices}/symbolic_name)
       node_name=$(cat /sys/class/fc_host/${hba_devices}/node_name)
       port_name=$(cat /sys/class/fc_host/${hba_devices}/port_name)
       curr_speed=$(cat /sys/class/fc_host/${hba_devices}/speed)
       fabric_id=$(cat /sys/class/fc_host/${hba_devices}/port_id)
       supp_speeds=$(cat /sys/class/fc_host/${hba_devices}/supported_speeds)
       port_state=$(cat /sys/class/fc_host/${hba_devices}/port_state)
       port_type=$(cat /sys/class/fc_host/${hba_devices}/port_type)
       echo "-----------------------------------------------"
       echo -e "Model:\t\t\t${model}"
       echo -e "Host Path:\t\t/sys/class/fc_host/${hba_devices}"
       echo -e "Firmware Version:\t${firmware_version}"
       echo -e "Driver Version:\t\t${driver_version}"
       echo -e "WWNN:\t\t\t${node_name}"
       echo -e "WWPN:\t\t\t${port_name}"
       echo -e "Current Speed:\t\t${curr_speed}"
       echo -e "Supported Speeds:\t${supp_speeds}"
       echo -e "Port Type:\t\t${port_type}"
       echo -e "SAN Fabric ID:\t\t${fabric_id}"
       echo -e "Current Port State:\t${port_state}"
       echo "-----------------------------------------------"
done
