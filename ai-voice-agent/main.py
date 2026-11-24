import webbrowser
import speech_recognition as sr

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
        print("NOVA: I couldn't understand that.")
        return ""

    except sr.RequestError:
        print("NOVA: Speech recognition service is unavailable.")
        return ""


while True:
    text = listen()

    if text in ("quit", "exit", "stop"):
        print("NOVA: Goodbye!")
        break

    if text:
        print("NOVA:", handle(text))









