using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// import for ros tcp connection  
using Unity.Robotics.ROSTCPConnector;
using RosTarget = RosMessageTypes.Unity.Vector3Msg;


public class RobotScript : MonoBehaviour
{
    Vector3 target;
    private Rigidbody _rigidbody;
    private Animator _animator;
    private int collisionDetected;
    
    float speed = 1.1f;
    // Start is called before the first frame update
    void Start()
    {
        collisionDetected = 0;
    target = transform.position;
     _animator = GetComponent<Animator>();
     _rigidbody = GetComponent<Rigidbody>();
     ROSConnection.GetOrCreateInstance().Subscribe<RosTarget>("Boss", locationChange);
        
        

    }
    
    public void OnCollisionEnter(Collision collision)
    {
        target = transform.position;
        collisionDetected = 1;
        Debug.Log("collision detected");
    }

    void locationChange(RosTarget target)
    {
        if (collisionDetected == 0){

            SetNewTarget(new Vector3(
                (float)target.pos_x,
                (float)target.pos_y,
                (float)target.pos_z
                )
        );
        }
        else {
             SetNewTarget(transform.position);

        }
        
        
    }
    // Update is called once per frame
    void FixedUpdate()
    {
     Debug.Log("Hello: " );
        Vector3 direction = target - transform.position;
        transform.Translate(direction.normalized * speed * Time.deltaTime, Space.World);
        //_rigidbody.MovePosition( _rigidbody.position - transform.forward * _SPEED * Time.fixedDeltaTime);
    }
    void SetNewTarget(Vector3 newTarget)
    {
        Debug.Log("Hello: " );
        target = newTarget;
        transform.LookAt(target);
        //_rigidbody.MovePosition( _rigidbody.position - transform.forward * speed * Time.fixedDeltaTime);

    }
}
