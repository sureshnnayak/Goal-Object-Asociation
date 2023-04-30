using UnityEngine;
using Unity.Robotics.ROSTCPConnector;
using RosColor = RosMessageTypes.UnityRoboticsDemo.UnityColorMsg;

using RosTarget = RosMessageTypes.Geometry.Vector3Msg;

public class RosSubscriber : MonoBehaviour
{
    public GameObject cube;

    void Start()
    {//The Subscribe<T>(string topicName, Action<T> callback) method is called on the ROSConnection instance. The T generic parameter specifies the message type that will be received on the subscribed topic
        ROSConnection.GetOrCreateInstance().Subscribe<RosColor>("color", ColorChange);
        ROSConnection.GetOrCreateInstance().Subscribe<RosColor>("target", Col);
    }

    void Col(RosColor targetMessage)
    {
        Debug.Log("Hello0000000000000000:");
        
    }

    void ColorChange(RosColor colorMessage)
    {

        cube.GetComponent<Renderer>().material.color = new Color32((byte)colorMessage.r, (byte)colorMessage.g, (byte)colorMessage.b, (byte)colorMessage.a);
    }
}