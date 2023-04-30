using UnityEngine;
using Unity.Robotics.ROSTCPConnector;
using RosMessageTypes.UnityRoboticsDemo;

/// <summary>
///
/// </summary>
public class ClairPublisher : MonoBehaviour
{
    ROSConnection ros;
    public string topicName = "AjLocation";

    // The game object
    public GameObject Aj;
    // Publish the Aj's position and rotation every N seconds
    public float publishMessageFrequency = 2.5f;

    // Used to determine how much time has elapsed since the last message was published
    private float timeElapsed;

    void Start()
    {
        // start the ROS connection
        ros = ROSConnection.GetOrCreateInstance();
        ros.RegisterPublisher<PosRotMsg>(topicName);
    }

    private void Update()
    {
        timeElapsed += Time.deltaTime;

        if (timeElapsed > publishMessageFrequency)
        {
            Aj.transform.rotation = Random.rotation;

            PosRotMsg AjPos = new PosRotMsg(
                Aj.transform.position.x,
                Aj.transform.position.y,
                Aj.transform.position.z,
                Aj.transform.rotation.x,
                Aj.transform.rotation.y,
                Aj.transform.rotation.z,
                Aj.transform.rotation.w
            );

            // Finally send the message to server_endpoint.py running in ROS
            ros.Publish(topicName, AjPos);

            timeElapsed = 0;
        }
    }
}
