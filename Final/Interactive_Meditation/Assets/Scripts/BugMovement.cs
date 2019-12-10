using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class BugMovement : MonoBehaviour
{
    public float timer;
    public int newtarget;
    public float speed;

    public NavMeshAgent nav;
    public Vector3 Target;
    // Start is called before the first frame update
    void Start()
    {

        nav = gameObject.GetComponent<NavMeshAgent>();

    }

    // Update is called once per frame
    void Update()
    {

        timer += Time.deltaTime;

        if(timer >= newtarget)
        {
            newTarget();
            timer = 0;

        }

        void newTarget() {

            float myx = gameObject.transform.position.x;
            float myz = gameObject.transform.position.z;

            float xPos = myx + Random.Range(myx - 100, myx + 100);
            float zPos = myz + Random.Range(myz - 100, myz + 100);

            Target = new Vector3(xPos, gameObject.transform.position.y, zPos);

            nav.SetDestination(Target);

        }


    }
}
