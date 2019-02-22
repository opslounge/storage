
# PureTEC Deploy storage playbook
This playbook calls 3 playbooks to create hosts, groups, and volumes
you can control the creation and deletion of objects with changes to the CSV file. 

# Using the CSV 
You can add new items in the "storage.csv" file ensure the format is as follows
id,wwna,wwnb,p_state,vol,size,hostg,proto,array,token

- id = hostname
- token = api token generated from user
- p_state = present/absent adds/removes items

# Running the playbook
ansible-playbook deploystorage.yaml

- include: addvol.yaml # adds a volume
- include: addhosts.yaml #adds a host and its wwns
- include: addhg.yaml # creates a host group and connects the hosts and volumes

# Requires the following library to run
https://github.com/mkouhei/ansible-role-includecsv
