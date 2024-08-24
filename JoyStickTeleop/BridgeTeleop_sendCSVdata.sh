#!/bin/bash

# Define variables
CSV_FILE="/home/esl/colcon_ws/src/My_ROS_Bridge/JoyStickTeleop/joy.csv"
INTERVAL=0.1  # Interval in seconds for sending the CSV file

# FTP server details
FTP_SERVER="192.168.1.33"  # IP of the FTP server
FTP_USERNAME="noeticpioneer"     
FTP_PASSWORD="esl"     
FTP_DEST_DIR="/home/noeticpioneer/My_ROS_Bridge/JoyStickTeleop/joy.csv"  # destination directory on the FTP server

# Function to send the file to the FTP server
send_to_ftp() {
    ftp -inv $FTP_SERVER <<EOF
user $FTP_USERNAME $FTP_PASSWORD
put $CSV_FILE $FTP_DEST_DIR 
bye
EOF
}

# Function to delete the file from the FTP server
delete_file_from_ftp() {
    ftp -inv $FTP_SERVER <<EOF
user $FTP_USERNAME $FTP_PASSWORD
delete $FTP_DEST_DIR
bye
EOF
}

# Main loop
while true; do

    # Send the CSV file to the FTP server
    send_to_ftp
    echo "File sent."

    # Wait for the specified interval before the next iteration
    sleep $INTERVAL
done
