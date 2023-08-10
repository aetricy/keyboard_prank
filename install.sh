#!/usr/bin/bash

pip install pygame
pip install pynput


sudo cat > config.py <<EOF
PATH="`pwd`"
EOF

sudo cat > delete.sh <<EOF
#!/bin/bash
echo "-----------------------------"
echo "Press END key to STOP Service"
echo "-----------------------------"
sudo systemctl stop keyboard_prank
sudo rm /etc/systemd/system/keyboard_prank.service
sudo rm /home/arslan/Documents/VisualCode/keyboard_prank"/config.py"
sudo systemctl daemon-reload 
echo " "
echo "-----------------------------"
echo "The Service Deleted."
echo "-----------------------------"
sudo rm delete.sh

EOF

if [ -z "$DATA_FILE" ]; then
    echo "Starting..."
fi


# remove the double quotes
DESCRIPTION="keyboard_prank"
SERVICE_NAME="keyboard_prank"
PKG_PATH="/usr/bin/python3"
SERVICE_PATH=`pwd`"/main.py"


# check if service is active
IS_ACTIVE=$(sudo systemctl is-active $SERVICE_NAME)
if [ "$IS_ACTIVE" == "active" ]; then
    # restart the service
    echo "Service is running"
    echo "Restarting service"
    sudo systemctl restart $SERVICE_NAME
    echo "Service restarted"
else
    # create service file
    echo "Creating service file"
    sudo cat > /etc/systemd/system/${SERVICE_NAME//'"'/}.service << EOF
[Unit]
Description=$DESCRIPTION
After=network.target
[Service]
ExecStart=$PKG_PATH $SERVICE_PATH
Restart=on-failure
[Install]
WantedBy=multi-user.target
EOF
    sudo systemctl daemon-reload 
    sudo systemctl enable ${SERVICE_NAME//'.service'/} # remove the extension
    sudo systemctl start ${SERVICE_NAME//'.service'/}
    echo "Service Started"
fi


sudo chmod +x main.py
sudo chmod +x install.sh
sudo chmod +x config.py
sudo chmod +x delete.sh

exit 0