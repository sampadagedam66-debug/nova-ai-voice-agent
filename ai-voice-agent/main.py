import webbrowser
import speech_recognition as sr
import pyttsx3

SITES = {
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "google": "https://www.google.com",
    "instagram": "https://www.instagram.com",
    "gmail": "https://mail.google.com",
    "spotify": "https://open.spotify.com",
    "linkedin": "https://www.linkedin.com",
    "chatgpt": "https://chatgpt.com",
}

# Text-to-speech setup
engine = pyttsx3.init()
engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)


# Nova speaks
def speak(message: str) -> None:
    engine.say(message)
    engine.runAndWait()


# Handle commands
def handle(command: str) -> str:
    command = command.lower().strip()

    if "open" in command:
        for name, url in SITES.items():
            if name in command:
                webbrowser.open(url)
                return f"Opening {name}"

        return "I don't know that website yet"

    return "Sorry, I can't do that yet"


# Listen to voice
def listen() -> str:
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("NOVA: Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower().strip()

    except sr.UnknownValueError:
        return "unrecognized"

    except sr.RequestError:
        return "service_error"


# Main program
speak("Hello! I am Nova. How can I help you?")

while True:
    text = listen()

    if text in ("quit", "exit", "stop"):
        speak("Goodbye!")
        print("NOVA: Goodbye!")
        break

    elif text == "unrecognized":
        speak("Sorry, I didn't understand that.")

    elif text == "service_error":
        speak("Speech recognition service is unavailable.")

    elif text:
        response = handle(text)
        print("NOVA:", response)
        speak(response)