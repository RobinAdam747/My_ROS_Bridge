#!/usr/bin/env python

import rospy
import csv
from sensor_msgs.msg import Joy
import time

class JoyDataPublisher:
    def __init__(self):
        # Initialize the ROS node
        rospy.init_node('joy_from_ROS2_publisher', anonymous=True)
        
        # Create a publisher object to publish to the Husky's joy topic
        self.pub = rospy.Publisher('/joy_data_from_ROS2', Joy, queue_size=10)
        
        # Set up a timer to call the callback function at the desired rate
        publish_interval = 1  # 1 Hz
        rospy.Timer(rospy.Duration(publish_interval), self.timer_callback)
        
        # Keep the node running
        rospy.spin()
    
    def load_csv_data(self, csv_file_path):
        try:
            with open(csv_file_path, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                next(csvreader, None)  # Skip the header row if there is one
                return next(csvreader, None)  # Read only the first row
        except FileNotFoundError:
            rospy.logerr("CSV file not found: {}".format(csv_file_path))
            return None
        except Exception as e:
            rospy.logerr("Error reading CSV file: {}".format(e))
            return None
    
    def timer_callback(self, event):
        csv_file_path = '/home/noeticpioneer/My_ROS_Bridge/JoyStickTeleop/joy.csv'
        row = self.load_csv_data(csv_file_path)
        
        if not row:
            rospy.logwarn("No data loaded from CSV file.")
            return
        
        # Create a Joy message
        joy_msg = Joy()
        
        # Populate the header with timestamp and frame_id
        joy_msg.header.stamp = rospy.Time.from_sec(float(row[0]))
        joy_msg.header.frame_id = row[1]
        
        # Convert the next N columns to axes (floats)
        joy_msg.axes = [float(value) for value in row[2:9]]
        
        # Convert the remaining columns to buttons (integers)
        joy_msg.buttons = [int(value) for value in row[10:]]
        
        # Publish the message
        self.pub.publish(joy_msg)

if __name__ == '__main__':
    try:
        JoyDataPublisher()
    except rospy.ROSInterruptException:
        pass