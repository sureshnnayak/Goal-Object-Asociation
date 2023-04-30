#!/usr/bin/env python3

import random
import rospy
import rosgraph
import time
from unity.msg import vector3

TOPIC_NAME = 'target'
#NODE_NAME = 'color_publisher'
NODE_NAME = 'terget_publisher'

def post_target():
    pub = rospy.Publisher(TOPIC_NAME, vector3, queue_size=10)
    rospy.init_node(NODE_NAME, anonymous=True)

    x = random.randint(0, 10)
    y = 0
    z = random.randint(0, 10)
    color = vector3(x, y, z)

    wait_for_connections(pub, TOPIC_NAME)
    pub.publish(color)

    time.sleep(0.1)


def wait_for_connections(pub, topic):
    ros_master = rosgraph.Master('/rostopic')
    topic = rosgraph.names.script_resolve_name('rostopic', topic)
    num_subs = 0
    for sub in ros_master.getSystemState()[1]:
        if sub[0] == topic:
            num_subs+=1

    for i in range(10):
        if pub.get_num_connections() == num_subs:
            return
        time.sleep(0.1)
    raise RuntimeError("failed to get publisher")


if __name__ == '__main__':
    try:
        post_target()
    except rospy.ROSInterruptException:
        pass