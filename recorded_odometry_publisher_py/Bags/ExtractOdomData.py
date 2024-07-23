import bagpy    # BagPy is the utility to manipulate rosbags
from bagpy import bagreader # BagReader is the utility to extract the csv from the rosbag
import pandas as pd

# Create a bagreader object
b = bagreader("Odometry.bag")
# b.topic_table

# Extract the odometry messages
odometryMsgs = b.odometry_data()
# odometryMsgs

# Create csv of the odometry messages
odometryData = pd.read_csv(odometryMsgs[0])
# odometryData