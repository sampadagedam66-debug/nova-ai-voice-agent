import webbrowser

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


while True:
    text = input("You: ").lower().strip()

    if text in ("quit", "exit"):
        print("NOVA: Goodbye!")
        break

    print("NOVA:", handle(text))









