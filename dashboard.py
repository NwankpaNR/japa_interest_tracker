import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Load data
wiki_df = pd.read_csv("data/wikipedia_views.csv")
reddit_df = pd.read_csv("data/reddit_posts.csv")

# Format dates
wiki_df["date"] = pd.to_datetime(wiki_df["date"].astype(str), format="%Y%m%d")

wiki_df = wiki_df.sort_values("date")
reddit_df["created_utc"] = pd.to_datetime(reddit_df["created_utc"])

# Sidebar
st.sidebar.title("🧭 JAPA Tracker")
selected_pages = st.sidebar.multiselect(
    "Select Wikipedia pages to compare:",
    sorted(wiki_df["page"].unique()),
    default=["Nigerian_diaspora", "Immigration_to_Canada"]
)

selected_regions = st.sidebar.multiselect(
    "Select Reddit regions:",
    sorted(reddit_df["region"].unique()),
    default=["Canada", "UK"]
)

# Main title
st.title("📈 How Public Interest in ‘JAPA’ Evolved")
st.caption("Data from Wikipedia pageviews & Reddit discussions")

# === Wikipedia Chart ===
st.subheader("Wikipedia Pageviews Over Time")
wiki_filtered = wiki_df[wiki_df["page"].isin(selected_pages)]
wiki_grouped = (
    wiki_filtered.groupby(["date", "page"], as_index=False)
    .agg({"views": "sum"})
)
wiki_grouped["date"] = pd.to_datetime(wiki_grouped["date"])

st.write("🧪 Column types:", wiki_grouped.dtypes)


fig1 = px.line(
    wiki_grouped,
    x="date",
    y="views",
    color="page",
    markers=True,
    title="Daily Wikipedia Pageviews"
)

fig1.update_layout(
    xaxis_title="Date",
    xaxis_type="date",  # ← this is key
    yaxis_title="Views",
    legend_title="Wikipedia Page"
)

fig1.update_xaxes(
    tickformat="%Y-%m-%d",     # show full date
    tickangle=45,              # rotate for readability
    showgrid=True,
    ticks="outside",
    tickfont=dict(size=10)
)


st.plotly_chart(fig1, use_container_width=True)

# === Reddit Mentions Chart ===
st.subheader("Reddit Mentions of 'JAPA' Over Time")

reddit_filtered = reddit_df[reddit_df["region"].isin(selected_regions)]
reddit_counts = reddit_filtered.groupby(["created_utc", "region"]).size().reset_index(name="mentions")

fig2 = px.bar(
    reddit_counts,
    x="created_utc",
    y="mentions",
    color="region",
    title="Daily Reddit Mentions by Region"
)
st.plotly_chart(fig2, use_container_width=True)

# === Footer ===
st.markdown("---")
st.markdown("📘 Wikipedia data via Wikimedia API | 🧵 Reddit data via PRAW")

