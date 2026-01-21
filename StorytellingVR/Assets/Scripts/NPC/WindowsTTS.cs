using System.Diagnostics;
using UnityEngine;

public static class WindowsTTS
{
    public static void Speak(string text)
    {
        if (string.IsNullOrWhiteSpace(text))
            return;

        text = text.Replace("\"", "").Replace("'", "");

        string command =
            "Add-Type -AssemblyName System.Speech;" +
            "$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer;" +
            "$speak.Rate = -1;" +
            "$speak.Volume = 100;" +
            "$speak.Speak('" + text + "');";

        ProcessStartInfo psi = new ProcessStartInfo
        {
            FileName = "powershell.exe",
            Arguments = "-NoProfile -STA -Command \"" + command + "\"",
            UseShellExecute = false,
            CreateNoWindow = true
        };

        Process.Start(psi);
    }
}
