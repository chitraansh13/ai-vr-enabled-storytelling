using UnityEngine;

public class SimpleFPSController : MonoBehaviour
{
    public float speed = 5.0f;
    public float sensitivity = 2.0f;
    CharacterController controller;
    Vector3 moveDirection;
    float rotationX = 0;

    void Start()
    {
        controller = GetComponent<CharacterController>();
        Cursor.lockState = CursorLockMode.Locked; // Locks mouse to screen
    }

    void Update()
    {
        // Rotation
        rotationX -= Input.GetAxis("Mouse Y") * sensitivity;
        rotationX = Mathf.Clamp(rotationX, -90, 90);
        Camera.main.transform.localRotation = Quaternion.Euler(rotationX, 0, 0);
        transform.rotation *= Quaternion.Euler(0, Input.GetAxis("Mouse X") * sensitivity, 0);

        // Movement
        float forward = Input.GetAxis("Vertical") * speed;
        float side = Input.GetAxis("Horizontal") * speed;
        moveDirection = (transform.forward * forward) + (transform.right * side);
        controller.SimpleMove(moveDirection);
    }
}