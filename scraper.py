import praw
from dotenv import load_dotenv
import os

# Load keys from .env
load_dotenv()

def get_reddit_instance():
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

def fetch_user_content(username, post_limit=50, comment_limit=100):
    reddit = get_reddit_instance()
    user = reddit.redditor(username)

    submissions = []
    comments = []

    # Get recent submissions (posts)
    for submission in user.submissions.new(limit=post_limit):
        title = submission.title
        body = submission.selftext or ""
        submissions.append(f"POST: {title}\n{body}")

    # Get recent comments
    for comment in user.comments.new(limit=comment_limit):
        comments.append(f"COMMENT: {comment.body}")

    return submissions, comments

