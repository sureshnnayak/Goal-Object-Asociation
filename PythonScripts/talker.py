#!/usr/bin/env python
# license removed for brevity
import rospy
import random
from std_msgs.msg import String
from unity.msg import vector3
from unity_robotics_demo_msgs.msg import UnityColor

charester = ["Aj", "Amy", "boss", "Ch17", "clair", "david", "jose", "jose2", "megan", "peasant"]
locations = [[20,0,25], [20,0,-25], [-22,0,-5]]
import time
# def talker():
#     pub = rospy.Publisher('target', String, queue_size=10)
#     rospy.init_node('talker', anonymous=True)
#     rate = rospy.Rate(10) # 10hz
#     while not rospy.is_shutdown():
#         hello_str = "hello world %s" % rospy.get_time()


#         x = random.randint(0, 10)
#         y = 0
#         z = random.randint(0, 10)
#         color = vector3(x, y, z)


#         rospy.loginfo(color)

#         pub.publish(hello_str)
#         rate.sleep()
#         time.sleep(5)



def sendCol():
    pub = rospy.Publisher('color', UnityColor, queue_size=10)
    pub2 = rospy.Publisher('target', vector3, queue_size=10)

    Aj    = rospy.Publisher('Aj', vector3, queue_size=10)
    Amy   = rospy.Publisher('Amy', vector3, queue_size=10)
    boss  = rospy.Publisher('Boss', vector3, queue_size=10)
    Ch17  = rospy.Publisher('Ch17', vector3, queue_size=10)
    clair = rospy.Publisher('Clair', vector3, queue_size=10)
    david = rospy.Publisher('David', vector3, queue_size=10)
    jose  = rospy.Publisher('Jose', vector3, queue_size=10)
    josh = rospy.Publisher('Josh', vector3, queue_size=10)
    josh2 = rospy.Publisher('Josh2', vector3, queue_size=10)
    megan = rospy.Publisher('Megan', vector3, queue_size=10)
    peasant  = rospy.Publisher('Peasant', vector3, queue_size=10)
    
    charecters = [Aj, Amy, boss, Ch17, clair, david, jose, josh, josh2, megan, peasant]

    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        print(hello_str)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = UnityColor(r, g, b, 1)
        # x = random.randint(0, 10)
        # y = 0
        # z = random.randint(0, 10)
        # color = vector3(x, y, z)
        
        x = locations[0][0]
        z = locations[0][2]
        y = 0
       
        for i in range(len(charecters)):
            if i >3:

                x = locations[1][0]
                z = locations[1][2]
            if i >6:

                x = locations[2][0]
                z = locations[2][2]
            pos = vector3(x, y, z)
            charecters[i].publish(pos)
            pub.publish(color)

        #pub2.publish(pos)
        

        
        
        rate.sleep()
        time.sleep(10)
    
if __name__ == '__main__':
    try:
        #talker()
        sendCol()
    except rospy.ROSInterruptException:
        pass