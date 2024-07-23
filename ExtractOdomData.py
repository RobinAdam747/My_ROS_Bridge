import bagpy
from bagpy import bagreader
import pandas as pd

b = bagreader("2024-07-17-10-14-34.bag")
# b.topic_table

odometryMsgs = b.odometry_data()
# odometryMsgs

odometryData = pd.read_csv(odometryMsgs[0])
# odometryData