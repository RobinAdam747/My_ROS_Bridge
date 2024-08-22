import bagpy    # BagPy is the utility to manipulate rosbags
from bagpy import bagreader # BagReader is the utility to extract the csv from the rosbag
import pandas as pd

def main():

    # Create a bagreader object
    b = bagreader(bagfile="OdometryAndTF.bag")

    # Extract the odometry and transform messages 
    odometryMsgs = b.message_by_topic(topic="/RosAria/pose")
    tfMsgs = b.message_by_topic(topic="/tf")

    # Create csv's of the odometry and transform messages
    odometryData = pd.read_csv(odometryMsgs[0])
    tfData = pd.read_csv(tfMsgs[0])

if __name__ == "__main__":
    main()
