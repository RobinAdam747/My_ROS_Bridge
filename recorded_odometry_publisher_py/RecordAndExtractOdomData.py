import bagpy    # BagPy is the utility to manipulate rosbags
from bagpy import bagreader # BagReader is the utility to extract the csv from the rosbag
import pandas as pd

def main():

    # Create a bagreader object
    b = bagreader(bagfile="Bags/Odometry.bag")

    # Extract the odometry messages 
    odometryMsgs = b.message_by_topic(topic="/RosAria/pose")

    # Create csv of the odometry messages
    odometryData = pd.read_csv(odometryMsgs[0])

if __name__ == "__main__":
    main()
