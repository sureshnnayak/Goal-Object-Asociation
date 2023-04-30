

# To DO
Environment 1
1. create the layout and add objects

2. generateHeatMap():
    2.1 Create a dummy file to generate a heap map -- DONE
    2.2 Integrate it with ros output
    2.3 Get object location
     

3. getObjects()
    3.1 Send the location/object details
        3.1.1 create a ros message --Done
    3.2 get objects


Environment 2:
1. findObjects()
   1.1 send objects()
   1.2 get object location: ROS service

2. getEnvironmentSnapshot()
3. getDestination()


publish ROS messages:
getHumanLocation()
getRobotLocation()


# Runnig Ros client to see ros messages
```bash
    cd ~/catkin_ws/
    source devel/setup.sh 
    #in another terminal
    rosparam set ROS_IP 192.168.50.91
    roscore
```


adding maximo charecter
1. Download charecter(without skin) and its waling style 
2. Click on the charecter (asset). rig->AnimationTpe = Humanoid. Materials-> extract to material folder.
3. click on the animation type. Rig->source= chrecter name. Animations-> select loop time. 
4. create a animation controller. pull the walking style into it. 
5.  add the created controller to all the charecters.



To call the ros service : rosservice call /obj_pose_srv Cube


1. the class name and file name should match
2. To add any custom message to ROS, create a WS in carkin and build the srokspace then import the message in unity


ROS UNity setup : https://www.youtube.com/watch?v=pdMxLxolQuo


cd Py   