#!/usr/bin/env python3
from numpy import int32, uint32

import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64    # interface type
import random   # for generating random numbers for the simulated temperaature sensor

from nav_msgs.msg import Odometry

import pandas as pd

# class TemperatureSensorNode(Node):
#     def __init__(self):
#         # Initialise (constructor)
#         super().__init__("temperature_sensor")

#         # Publish function prototype kinda
#         self.temperature_publisher_ = self.create_publisher(
#             Int64, "temperature", 10)
        
#         # Timer to simulate a publishing frequency
#         self.temperature_timer_ = self.create_timer(
#             2.0, self.publish_temperature)
        
#     # Definition of publish function
#     def publish_temperature(self):
#         temperature = random.randint(20, 30)    # random number between 20 and 30 to simulate temperature measurement
        
#         msg = Int64()   # message type
#         msg.data = temperature  # message data
#         self.temperature_publisher_.publish(msg)    # ROS publish method


class OdometryNode(Node):
    def __init__(self):
        # Initialise (constructor)
        super().__init__("robot_odometry")

        # Publish function prototype thing
        self.odometry_publisher_ = self.create_publisher(
            Odometry, "pose", 10)
        
        # Timer to set publish frequency
        self.odometry_timer_ = self.create_timer( 1.0, self.publish_odometry)

        # Publish on trigger...

    def publish_odometry(self):
        # Read in csv of recorded odometry
        odomData = pd.read_csv("recorded_odometry_publisher_py/Bags/Odometry/RosAria-pose.csv")

        # Define message type
        msg = Odometry()

        # Assign data to the message per column
        msg.header.frame_id = odomData.at[1, "header.frame_id"]
        msg.header.stamp.sec = int(odomData.at[1, "header.stamp.secs"])
        msg.header.stamp.nanosec = int(odomData.at[1, "header.stamp.nsecs"])
        msg.child_frame_id = odomData.at[1, "child_frame_id"]
        msg.pose.pose.orientation.w = odomData.at[1, "pose.pose.orientation.w"]
        msg.pose.pose.orientation.x = odomData.at[1, "pose.pose.orientation.x"]
        msg.pose.pose.orientation.y = odomData.at[1, "pose.pose.orientation.y"]
        msg.pose.pose.orientation.z = odomData.at[1, "pose.pose.orientation.z"]
        msg.pose.pose.position.x = odomData.at[1, "pose.pose.position.x"]
        msg.pose.pose.position.y = odomData.at[1, "pose.pose.position.x"]
        msg.pose.pose.position.z = odomData.at[1, "pose.pose.position.z"]
        # msg.pose.covariance = odomData.at[1, "pose.covariance"]
        msg.twist.twist.linear.y = odomData.at[1, "twist.twist.linear.y"]
        msg.twist.twist.linear.z = odomData.at[1, "twist.twist.linear.y"]
        msg.twist.twist.linear.x = odomData.at[1, "twist.twist.linear.z"]
        msg.twist.twist.angular.y = odomData.at[1, "twist.twist.angular.y"]
        msg.twist.twist.angular.x = odomData.at[1, "twist.twist.angular.x"]
        msg.twist.twist.angular.z = odomData.at[1, "twist.twist.angular.z"]
        # msg.twist.covariance = odomData.at[1, "twist.covariance"]
        
        self.odometry_publisher_.publish(msg)   # ROS publish method

def main(args=None):
    rclpy.init(args=args)
    node = OdometryNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()