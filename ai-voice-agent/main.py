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

engine = pyttsx3.init()
engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)


def speak(message: str) -> None:
    engine.say(message)
    engine.runAndWait()


def handle(command: str) -> str:
    if command.startswith("open "):
        name = command.removeprefix("open ").strip()

        if name in SITES:
            webbrowser.open(SITES[name])
            return f"Opening {name}"

        return f"I don't know {name} yet"

    return "Sorry, I can't do that yet"


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









