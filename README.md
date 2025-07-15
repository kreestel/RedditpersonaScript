# Reddit Persona Analyzer 

This project creates detailed user personas from Reddit profiles using scraped post and comment data, with LLM-powered analysis via OpenAI API.


## WorkFlow
- Scrapes a Reddit user's recent posts and comments using the Reddit API (via `praw`)
- Sends content to GPT-3.5 to generate a structured, insight-rich persona
- Outputs persona as a `.txt` file with cited quotes and behavioral analysis.

---

## How to Run Locally

### 1. Clone the repo & set up environment
```bash
git clone https://github.com/yourusername/reddit-persona
cd reddit-persona
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
```
### 2. Create a .env file with your API keys:
```bash
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_custom_user_agent
OPENAI_API_KEY=your_openai_key
```
### 3. Run the script
```bash 
python main.py
```
---
Built As part of BeyondChats’ AI/LLM Assessment. 
