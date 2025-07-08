import requests
import pandas as pd
from datetime import datetime, timedelta
import os

# Pages to track
pages = [
    "Demographics_of_Nigeria",
    "Nigerian_diaspora",
    "Immigration_to_Canada",
    "Immigration_to_the_United_Kingdom",
    "Right_of_asylum",  # General
    "Brain_drain"       # Related
]

from urllib.parse import quote

def fetch_pageviews(page, start_date, end_date):
    page_encoded = quote(page)
    url = (
        f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article"
        f"/en.wikipedia.org/all-access/all-agents/{page_encoded}/daily/{start_date}/{end_date}"
    )

    headers = {
        "User-Agent": "japa-interest-tracker/1.0 (Nkiru; contact: vushakes@gmail.com)"
    }

    try:
        res = requests.get(url, headers=headers)
        print(f"📡 Requesting: {url} → Status: {res.status_code}")
        res.raise_for_status()

        data = res.json()
        views = []
        for item in data.get("items", []):
            views.append({
                "page": page,
                "date": item["timestamp"][:8],
                "views": item["views"]
            })
        return views

    except Exception as e:
        print(f"❌ Failed to fetch pageviews for {page}: {e}")
        return []



if __name__ == "__main__":
    today = datetime.utcnow().date()
    start = (today - timedelta(days=365)).strftime("%Y%m%d")
    end = today.strftime("%Y%m%d")

    all_views = []
    for page in pages:
        print(f"📘 Fetching Wikipedia views for {page}...")
        all_views.extend(fetch_pageviews(page, start, end))

    df = pd.DataFrame(all_views)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/wikipedia_views.csv", index=False)
    print("✅ Wikipedia data saved to data/wikipedia_views.csv")
