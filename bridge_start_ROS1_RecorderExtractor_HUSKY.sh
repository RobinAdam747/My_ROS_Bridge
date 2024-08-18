#!/bin/bash
# Startup of bridge (ROS1)
source /opt/ros/melodic/setup.bash

while true; do
	# start the rosbag recording
	rosbag record --duration=0.3 -O ~/My_ROS_Bridge/recorded_odometry_publisher_py/Bags/Odometry.bag /husky_velocity_controller/odom

	# Run recorder-extractor script:
	python3 /home/administrator/My_ROS_Bridge/recorded_odometry_publisher_py/RecordAndExtractOdomData.py
done
