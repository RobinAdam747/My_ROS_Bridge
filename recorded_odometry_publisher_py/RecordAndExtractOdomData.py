import bagpy    # BagPy is the utility to manipulate rosbags
from bagpy import bagreader # BagReader is the utility to extract the csv from the rosbag
import pandas as pd
import subprocess
import time

import subprocess
import time

def start_recording(bag_name):
    # Start recording a ROS bag
    # RooiBot:
    return subprocess.Popen(['rosbag', 'record', '-O', bag_name, '/RosAria/pose'])
    # Husky:
    # return subprocess.Popen(['rosbag', 'record', '-O', bag_name, '/husky_velocity_controller/odom'])

def stop_recording(process):
    # Stop recording the ROS bag
    process.terminate()
    process.wait()

def main():
    interval = 0.1  # Time in seconds to record
    # bag_counter = 0

    while True:
        bag_name = "Odometry.bag"
        print(f"Starting recording: {bag_name}")
        process = start_recording(bag_name)
        
        time.sleep(interval)
        
        print(f"Stopping recording: {bag_name}")
        stop_recording(process)
        
        bag_counter += 1
        # time.sleep(1)  # Wait before starting the next recording

        # Create a bagreader object
        b = bagreader(bagfile="Bags/Odometry.bag")

        # Extract the odometry messages 
        odometryMsgs = b.message_by_topic(topic="/RosAria/pose")

        # Create csv of the odometry messages
        odometryData = pd.read_csv(odometryMsgs[0])

if __name__ == "__main__":
    main()