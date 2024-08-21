#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
import csv
from threading import Timer

# Define the CSV file path
csv_file_path = 'joy.csv' 

# Define the interval for overwriting the CSV file (in seconds)
overwrite_interval = 5

class JoySubscriber(Node):

    def __init__(self):
        super().__init__('joy_subscriber_to_csv')
        self.subscription = self.create_subscription(
            Joy,
            '/joy',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Write the initial header
        self.write_header()

        # Start the periodic overwrite
        self.periodic_overwrite()

    def write_header(self):
        # Create the CSV file and write the header
        with open(csv_file_path, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            # Write the header row (modify according to your message structure)
            header = ['axes_{}'.format(i) for i in range(8)] + ['button_{}'.format(i) for i in range(11)]
            csvwriter.writerow(header)

    def listener_callback(self, msg):
        # Open the CSV file in append mode
        with open(csv_file_path, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            
            # Write the message data to the CSV file
            # Flatten the axes and buttons arrays into a single row
            row = list(msg.axes) + list(msg.buttons)
            csvwriter.writerow(row)

    def periodic_overwrite(self):
        # Write the header to overwrite the CSV file
        self.write_header()
        
        # Schedule the next overwrite
        Timer(overwrite_interval, self.periodic_overwrite).start()

def main(args=None):
    rclpy.init(args=args)
    joy_subscriber = JoySubscriber()
    rclpy.spin(joy_subscriber)

    # Destroy the node explicitly
    joy_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()