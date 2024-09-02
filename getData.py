#!/usr/bin/env python
 
import rospy
from xela_server.srv import XelaSensorXYZ
from xela_server.msg import xServerMsg
 
def callback(xeladata):
    # print("--- data is: -----------------------------")
    # print(xeladata)
  
  if xeladata.sensor == 2:
    print("left: ",xeladata.points[9])
    print("-----------------------------")
  # if xeladata.sensor == 2:
  #   print("right: ",xeladata.points[9])
  #   print("-----------------------------")
 
rospy.init_node('xela_xr2244_sensor')
rospy.Subscriber('/xServTopic', xServerMsg, callback)
 

rospy.spin()

# rosbag record /camera/color/image_raw /sensor_camera_16june /sensor_data_16june
# rostopic hz /camera/color/image_raw
# roslaunch realsense2_camera rs_camera.launch
# rosbag record /camera/color/image_raw /xServTopic