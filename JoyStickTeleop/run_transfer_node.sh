#!/bin/bash
# Setup for joystick
# joystick node to get messages from controller
#rosrun joy joy_node
# script to transfer messages to husky joystick teleop node
python /home/administrator/transfer_joy_msgs_to_husky.py
