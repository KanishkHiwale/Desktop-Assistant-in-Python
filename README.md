# Desktop-Assistant-in-Python
This project is a Python-based voice assistant that can communicate in both English and Marathi, allowing users to interact through voice commands. The assistant is designed to handle various tasks such as:

- **Language Switching:** Users can toggle between English and Marathi modes. The assistant starts in English by default but can switch to Marathi based on user preference.
- **Information Retrieval:** The assistant can fetch information from Wikipedia based on voice input, making it easy to gather knowledge on various topics.
- **YouTube Playback:** Users can ask the assistant to play videos on YouTube, specifying the video content through voice commands.
- **Google Search:** The assistant can perform Google searches, providing a quick way to find information online.
- **Time and Date:** It can tell the current time and date.
- **Opening Applications:** The assistant can open system applications based on voice commands.
- **Exit Command:** Users can close the assistant by giving a command to quit or exit.

## Important Libraries to Install

Before running the project, make sure to install the following libraries:

```bash
pip install pyttsx3 SpeechRecognition selenium google-api-python-client
```

### Additional Setup

- **Pyttsx3:** Used for text-to-speech conversion, enabling the assistant to speak out responses.
- **SpeechRecognition:** Allows the assistant to process and understand voice commands.
- **Selenium:** Used for web automation, especially for tasks like YouTube playback and Google searches.
- **Google API Client:** Used for integrating with Google services if needed for more advanced features.

To install these libraries, you can use the provided `pip install` command.
