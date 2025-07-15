import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_persona(username, submissions, comments):
    content = "\n\n".join(submissions + comments)


    max_chars = 12000
    content = content[:max_chars]

    prompt = f"""
You are an expert in digital behavior analysis.

Using the following Reddit posts and comments from user u/{username}, generate a detailed and structured user persona. Use only the information present in the content — do not make up facts.

Output the persona in this format:

USER PERSONA: u/{username}

👤 BASIC INFO
- Age: 
- Occupation:
- Status:
- Location:
- Archetype:
- Tier:

💡 ATTRIBUTES
- [trait] | [trait] | [trait] | [trait]

🔥 MOTIVATIONS
- [Explain motivations from patterns and quotes]

🧠 PERSONALITY
- Introvert/Extrovert: 
- Intuition/Sensing: 
- Feeling/Thinking: 
- Perceiving/Judging: 

🧍‍♂️ BEHAVIOUR & HABITS
- [How they browse, post, comment, etc.]

💢 FRUSTRATIONS
- [What they dislike or complain about]

🎯 GOALS & NEEDS
- [What they aim to achieve, learn, fix, etc.]

📎 CITED POSTS & COMMENTS
- "Exact quote here" – subreddit name (post or comment)

Reddit content:
\"\"\"
{content}
\"\"\"
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response['choices'][0]['message']['content']
