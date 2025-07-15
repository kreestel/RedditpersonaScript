from scraper import fetch_user_content
from persona_generator import generate_persona
import os

def save_output(username, persona_text):
    os.makedirs("output", exist_ok=True)
    with open(f"output/u_{username}_persona.txt", "w", encoding="utf-8") as f:
        f.write(persona_text)

if __name__ == "__main__":
    profile_url = input("Enter Reddit profile URL: ").strip()
    username = profile_url.rstrip("/").split("/")[-1]

    print(f"Fetching data for: u/{username}")
    posts, comments = fetch_user_content(username)

    print(f"Generating persona for u/{username}...")
    persona_text = generate_persona(username, posts, comments)

    save_output(username, persona_text)
    print(f"Persona saved: output/u_{username}_persona.txt")
