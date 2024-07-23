import bagpy
from bagpy import bagreader
import pandas as pd

b = bagreader("Odometry.bag")
# b.topic_table

odometryMsgs = b.odometry_data()
# odometryMsgs

odometryData = pd.read_csv(odometryMsgs[0])
# odometryData