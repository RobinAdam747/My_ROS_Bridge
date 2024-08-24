#!/usr/bin/env python

import rospy
import csv
from sensor_msgs.msg import Joy

def csv_publisher():
    # Initialize the ROS node
    rospy.init_node('joy_from_ROS2_publisher', anonymous=True)
    
    # Create a publisher object to publish to the Husky's joy topic
    pub = rospy.Publisher('/joy_data_from_ROS2', Joy, queue_size=10)
    
    # Set the rate at which to publish messages
    rate = rospy.Rate(0.1)  # 10 Hz
    
    # Path to the CSV file
    csv_file_path = '/home/noeticpioneer/My_ROS_Bridge/JoyStickTeleop/joy.csv'

    # Making sure the node is not going to stop if it doesn't find data on startup
    file_read_success = False
    
    while not rospy.is_shutdown():
        while not file_read_success:
            try:
                # Open the CSV file
                with open(csv_file_path, 'r') as csvfile:
                    csvreader = csv.reader(csvfile)

                    # Loop exit once joy data found
                    file_read_success = True
                    
                    # Skip the header row if there is one
                    next(csvreader, None)
                    
                    # Loop through the rows in the CSV file
                    for row in csvreader:
                        if rospy.is_shutdown():
                            break
                        
                        # Create a Joy message
                        joy_msg = Joy()
                        
                        # Assuming the CSV has columns for axes and buttons
                        # Example: axes1, axes2, ..., button1, button2, ...
                        # Modify the following lines according to your CSV structure
                        
                        # Convert the first N columns to axes (floats)
                        joy_msg.axes = [float(value) for value in row[:8]]
                        
                        # Convert the remaining columns to buttons (integers)
                        joy_msg.buttons = [int(value) for value in row[8:]]
                        
                        # Publish the message
                        pub.publish(joy_msg)
                        
                        # Sleep to maintain the loop rate
                        rate.sleep()
            
            except FileNotFoundError:
                rospy.logwarn("CSV file not found, retrying...")
                rate.sleep()
            except Exception as e:
                rospy.logerr("Error reading CSV file")
                rate.sleep()

if __name__ == '__main__':
    try:
        csv_publisher()
    except rospy.ROSInterruptException:
        pass
