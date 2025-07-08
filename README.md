# 🧭 How Public Interest in “JAPA” Evolved: A Wikipedia & Reddit Data Dashboard

This interactive dashboard explores how Nigerian migration culture — popularly known as **"JAPA"** — has been reflected in online interest over time.

Using Wikipedia pageviews and Reddit search trends, we compare migration discussions across the **UK**, **Canada**, and **other Nigerian diaspora forums**.

---

## 🔍 Features

- 📈 Trends in Wikipedia pageviews for migration-related articles
- 🔎 Reddit mentions of "japa" across r/nigeria, r/ukvisa, r/ImmigrationCanada, etc.
- 🗺️ Region-based comparison (UK, Canada, Other)
- 📅 Time-series filtering for custom exploration

---

## ⚙️ Tech Stack

| Layer        | Tool/Library               |
|--------------|----------------------------|
| Web App      | Streamlit                  |
| Data Viz     | Plotly Express             |
| Reddit API   | `praw` + subreddit search  |
| Wikipedia    | Wikimedia Pageviews API    |
| Scheduler    | Manual / CLI (Python)      |
| Format/Env   | `.env`, `pandas`, `requests` |

---

## 🚀 Getting Started

### 1. Clone the Repo

git clone https://github.com/yourusername/japa-interest-tracker.git

cd japa-interest-tracker

###  2. Install Dependencies

pip install -r requirements.txt

###  3. Create .env File

REDDIT_CLIENT_ID=your_id

REDDIT_CLIENT_SECRET=your_secret

REDDIT_USER_AGENT=japa-tracker-bot

###  4. Run Data Collectors

python wiki_tracker.py

python reddit_tracker.py

###  5. Launch Dashboard

streamlit run dashboard.py

# Insights to Explore

When did online interest in "japa" spike?

Are migration discussions more active in Canada or UK Reddit communities?

What topics (e.g. asylum, brain drain) align with emigration patterns?

# TODOS and Extensions

Add sentiment analysis of Reddit post titles

Incorporate Google Trends data

Compare JAPA-related hashtags from X (formerly Twitter)

# Acknowledgements

https://wikitech.wikimedia.org/wiki/Analytics/AQS/Pageviews

https://praw.readthedocs.io/
