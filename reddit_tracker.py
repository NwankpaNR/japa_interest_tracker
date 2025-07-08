import praw
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# Initialize Reddit API (read-only)
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# Subreddits to track
subreddits = {
    "nigeria": "Other",
    "ImmigrationCanada": "Canada",
    "ukvisa": "UK",
    "ukimmigration": "UK",
    "casualuk": "UK"
}

keyword = "japa"
posts = []

# Search each subreddit
keywords = ["japa", "nigeria", "migrate", "immigrate", "visa", "PR"]

for sub, region in subreddits.items():
    print(f"🔍 Searching r/{sub}...")
    for kw in keywords:
        for submission in reddit.subreddit(sub).search(kw, limit=50):
            posts.append({
                "id": submission.id,
                "title": submission.title,
                "score": submission.score,
                "created_utc": datetime.utcfromtimestamp(submission.created_utc).date(),
                "subreddit": sub,
                "region": region,
                "url": submission.url
            })


# Save to CSV
df = pd.DataFrame(posts)
os.makedirs("data", exist_ok=True)
df.to_csv("data/reddit_posts.csv", index=False)
print("✅ Reddit data saved to data/reddit_posts.csv")
print("📊 Region breakdown:")
print(df["region"].value_counts())
