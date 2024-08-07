#!/bin/bash
## Startup of bridge (ROS1)
# Sourcing the ROS1 workspace
source /opt/ros/noetic/setup.bash

# Sourcing ROSAria workspace
cd catkin_ws
. devel/setup.bash

# Start RosAria demo client
roslaunch rosaria_client rosaria_client_launcher.launch
