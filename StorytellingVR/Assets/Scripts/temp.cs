using UnityEngine;

public class GestureTest : MonoBehaviour
{
    Animator anim;

    void Start()
    {
        anim = GetComponent<Animator>();
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.G))
        {
            anim.SetTrigger("Gesture_Acknowledge");
        }

        if (Input.GetKeyDown(KeyCode.H))
        {
            anim.SetTrigger("Gesture_Happy");
        }

    }
}
