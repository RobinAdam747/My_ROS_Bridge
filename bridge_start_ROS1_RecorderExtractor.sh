#!/bin/bash
# Startup of bridge (ROS1)
source /opt/ros/noetic/setup.bash

while true; do
	# start the rosbag recording
	rosbag record --duration=0.3 -O /home/noeticpioneer/My_ROS_Bridge/recorded_odometry_publisher_py/Bags/Odometry.bag /RosAria/pose

	# Run recorder-extractor script:
	python3 /home/noeticpioneer/My_ROS_Bridge/recorded_odometry_publisher_py/RecordAndExtractOdomData.py
done
