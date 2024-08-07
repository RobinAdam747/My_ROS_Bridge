#!/bin/bash
# Startup of bridge (ROS2)
#python3 /home/esl/colcon_ws/src/My_ROS_Bridge/recorded_odometry_publisher_py/FTPinteraction.py

# FTP server details
SERVER="192.168.1.33"
USERNAME="noeticpioneer"
PASSWORD="esl"
REMOTE_FILE_PATH="/home/noeticpioneer/My_ROS_Bridge/recorded_odometry_publisher_py/Bags/Odometry/RosAria-pose.csv"
LOCAL_FILE_PATH="RosAria-pose.csv"

# Function to check if a file exists on the FTP server
file_exists_on_ftp() {
    ftp -inv $SERVER <<EOF | grep -q "226 Transfer complete"
user $USERNAME $PASSWORD
size $REMOTE_FILE_PATH
bye
EOF
}

# Function to fetch the file from the FTP server
fetch_file_from_ftp() {
    ftp -inv $SERVER <<EOF
user $USERNAME $PASSWORD
get $REMOTE_FILE_PATH $LOCAL_FILE_PATH
bye
EOF
}

# Function to delete the file from the FTP server
delete_file_from_ftp() {
    ftp -inv $SERVER <<EOF
user $USERNAME $PASSWORD
delete $REMOTE_FILE_PATH
bye
EOF
}

# Main loop
while true; do

	fetch_file_from_ftp
        echo "File fetched. Deleting the file on the server..."
    
    if file_exists_on_ftp; then
        echo "File exists. Fetching the file..."
        fetch_file_from_ftp
        echo "File fetched. Deleting the file on the server..."
        delete_file_from_ftp
        echo "File deleted on the server."
    else
        echo "File does not exist. Waiting..."
    fi
    sleep 0.1  # Wait for 0.1 second before checking again
done
