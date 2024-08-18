#!/bin/bash

# Define variables
BAG_FILE="recorded_data"
CSV_FILE="output_data.csv"
TOPIC="/your_topic_name"  # Replace with your actual topic name

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