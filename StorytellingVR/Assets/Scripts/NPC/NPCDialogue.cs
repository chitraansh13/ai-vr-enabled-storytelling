using System.Collections;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;

[System.Serializable]
public class PlayerMessage
{
    public string text;
}

[System.Serializable]
public class NPCResponse
{
    public string reply;
}

public class NPCDialogue : MonoBehaviour
{
    public Text dialogueText;
    public InputField playerInput;

    private string url = "http://127.0.0.1:8000/chat";

    public void SendPlayerQuestion()
    {
        if (string.IsNullOrWhiteSpace(playerInput.text))
            return;

        AskNPC(playerInput.text);
        playerInput.text = "";
    }

    void AskNPC(string question)
    {
        StartCoroutine(SendRequest(question));
    }

    IEnumerator SendRequest(string question)
    {
        PlayerMessage data = new PlayerMessage { text = question };
        string json = JsonUtility.ToJson(data);

        UnityWebRequest request = new UnityWebRequest(url, "POST");
        byte[] body = System.Text.Encoding.UTF8.GetBytes(json);

        request.uploadHandler = new UploadHandlerRaw(body);
        request.downloadHandler = new DownloadHandlerBuffer();
        request.SetRequestHeader("Content-Type", "application/json");

        yield return request.SendWebRequest();

        if (request.result == UnityWebRequest.Result.Success)
        {
            NPCResponse response =
                JsonUtility.FromJson<NPCResponse>(request.downloadHandler.text);

            dialogueText.text = "NPC: " + response.reply;
        }
        else
        {
            dialogueText.text = "NPC: (no response)";
        }
    }
}
