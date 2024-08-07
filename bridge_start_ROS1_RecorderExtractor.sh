#!/bin/bash
# Startup of bridge (ROS1)
source /opt/ros/noetic/setup.bash

while true; do
	# start the rosbag recording
	rosbag record -O Odometry.bag /RosAria/pose
	
	# wait a bit
	
	# stop the recording
	pkill -f "rosbag record -O Odometry.bag /RosAria/pose"

	# Run recorder-extractor script:
	python /home/esl/My_ROS_Bridge/recorded_odometry_publisher_py/RecordAndExtractOdomData.py
