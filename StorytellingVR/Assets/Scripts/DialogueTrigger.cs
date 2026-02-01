using UnityEngine;

public class DialogueTrigger : MonoBehaviour
{
    public GameObject dialogueCanvas; // Drag your Canvas here in the Inspector

    void Start()
    {
        dialogueCanvas.SetActive(false); // Hide it at the start
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            dialogueCanvas.SetActive(true);
            Cursor.lockState = CursorLockMode.None; // Let you use the mouse/keyboard
        }
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            dialogueCanvas.SetActive(false);
            Cursor.lockState = CursorLockMode.Locked; // Back to walking mode
        }
    }
}