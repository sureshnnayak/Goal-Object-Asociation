#!/usr/bin/env python
import rospy
from unity_robotics_demo_msgs.msg import PosRot
import matplotlib.pyplot as plt
import numpy as np


import time
  
Starttime = time.time()
# Generate some random data
x = []
y = []

def callback(data):
    x.append(int(data.pos_x) +30)
    y.append(int(data.pos_z)+30)
    #print(x,y)
    laptime = round((time.time() - Starttime), 2)
    if laptime > 300:
        print("printing the heat map")
        # Create a hexbin plot
        plt.hexbin(x, y, gridsize=20, cmap='inferno', bins='log', mincnt=1)

            # Add a colorbar
        plt.colorbar()

        # Set the axis labels and title
        plt.xlabel('X coordinate')
        plt.ylabel('Y coordinate')
        plt.title('Heatmap based on X-Y coordinates')
        plt.show()
        exit(0)
        return 0

    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)




    rospy.Subscriber("AjLocation", PosRot, callback)
    rospy.Subscriber("AmyLocation", PosRot, callback)
    rospy.Subscriber("BossLocation", PosRot, callback)
    rospy.Subscriber("Ch17Location", PosRot, callback)
    rospy.Subscriber("ClairLocation", PosRot, callback)
    rospy.Subscriber("DavidLocation", PosRot, callback)
    rospy.Subscriber("JoseLocation", PosRot, callback)
    rospy.Subscriber("Josh2Location", PosRot, callback)
    rospy.Subscriber("MeganLocation", PosRot, callback)
    rospy.Subscriber("PeasantLocation", PosRot, callback)
    rospy.Subscriber("RobotLocation", PosRot, callback)

    

    # Display the plot
    plt.show()
        

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
    

