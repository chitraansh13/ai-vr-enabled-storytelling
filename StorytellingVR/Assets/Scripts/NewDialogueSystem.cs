using UnityEngine;
using TMPro;

public class NewDialogueSystem : MonoBehaviour
{
    public GameObject myNewCanvas; // Drag the new Canvas here
    public TMP_Text npcTextMesh;    // Drag 'NPC_Text' here
    public TMP_InputField input;   // Drag 'Player_Input' here

    void Start()
    {
        myNewCanvas.SetActive(false); // Make sure it starts hidden
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            myNewCanvas.SetActive(true);
            Cursor.lockState = CursorLockMode.None;
            Cursor.visible = true;
            input.ActivateInputField(); // Automatically focus so you can type
        }
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            myNewCanvas.SetActive(false);
            Cursor.lockState = CursorLockMode.Locked;
            Cursor.visible = false;
        }
    }
}