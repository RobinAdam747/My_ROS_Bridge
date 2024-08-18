#!/bin/bash

# Define variables
BAG_FILE="~/esl/colcon_ws/src/My_ROS_Bridge/JoyStickTeleop/"
CSV_FILE="~/esl/colcon_ws/src/My_ROS_Bridge/JoyStickTeleop/joy.csv"
TOPIC="/joy"

# FTP server details
FTP_SERVER="ftp.yourserver.com"  # Replace with your FTP server address
FTP_USERNAME="your_username"     # Replace with your FTP username
FTP_PASSWORD="your_password"     # Replace with your FTP password
FTP_DEST_DIR="/path/to/destination"  # Replace with the destination directory on the FTP server

while true; do
    # Record the ROS2 bag for 1 second
    echo "Recording ROS2 bag for 1 second..."
    ros2 bag record -o $BAG_FILE -d 1 $TOPIC

    # Check if the bag file was created
    if [ ! -d "$BAG_FILE" ]; then
        echo "Failed to record ROS2 bag."
        exit 1
    fi

    echo "ROS2 bag recorded successfully."

    # Play back the ROS2 bag in the background
    echo "Playing back the ROS2 bag..."
    ros2 bag play $BAG_FILE --duration 1 &

    # Wait for a short period to ensure playback starts
    sleep 2

    # Convert the ROS2 bag to CSV
    echo "Converting ROS2 bag to CSV..."
    ros2 topic echo $TOPIC --qos-profile-overrides-path $BAG_FILE > $CSV_FILE

    # Check if the CSV file was created
    if [ ! -f "$CSV_FILE" ]; then
        echo "Failed to convert ROS2 bag to CSV."
        exit 1
    fi

    echo "CSV file created successfully: $CSV_FILE"

    # Send the CSV file to the FTP server
    echo "Sending CSV file to FTP server..."
    curl -T $CSV_FILE ftp://$FTP_USERNAME:$FTP_PASSWORD@$FTP_SERVER$FTP_DEST_DIR/

    if [ $? -eq 0 ]; then
        echo "CSV file sent successfully to FTP server."
    else
        echo "Failed to send CSV file to FTP server."
    fi

    # Optional: Add a sleep period between iterations
    sleep 1
done