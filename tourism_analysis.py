"""
Sustainable Tourism Sentiment Analysis — Wales social media analytics.
UKRI-funded research, Cardiff Metropolitan University.

Renders the ACTUAL sentiment breakdown computed in "Sustainable Tourism
Project.ipynb" (cell 21: TextBlob sentiment classification on a real
112,993-row tweet dataset loaded from a real tweets.xlsx export, cell 13
confirms the row count). These are not simulated — they are copied verbatim
from that notebook's own executed output.

Note: the notebook's loaded dataset spans roughly 2014-2023 (see the `date`
column in cell 6), not 2010-2020 — the topic-by-topic and year-by-year
breakdowns previously shown here (5 named topics, per-year trend, keyword
frequency table) do not exist anywhere in the notebook and have been
removed. The notebook's own further analysis (beyond overall sentiment %)
is a per-country choropleth map (cell 60), not a topic/topic-sentiment
breakdown.
"""

from __future__ import annotations

import os
import matplotlib.pyplot as plt

os.makedirs("outputs", exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})

# ---- Real results, copied from notebook cells 13 and 21 --------------------
TOTAL_TWEETS = 112_993
SENTIMENT = {"Positive": 52.58, "Neutral": 39.70, "Negative": 7.72}
sent_colors = {"Positive": "#2ecc71", "Neutral": "#95a5a6", "Negative": "#e74c3c"}

fig, ax = plt.subplots(figsize=(7, 7))
fig.suptitle(f"Wales Tourism Tweet Sentiment (real, TextBlob, n={TOTAL_TWEETS:,})",
             fontsize=12, fontweight="bold")
ax.pie(SENTIMENT.values(), labels=SENTIMENT.keys(),
       colors=[sent_colors[k] for k in SENTIMENT],
       autopct="%1.1f%%", startangle=90, wedgeprops={"edgecolor": "white"})

plt.savefig("outputs/01_sentiment_analysis.png", dpi=150, bbox_inches="tight")
plt.close()
print("[PLOT]  outputs/01_sentiment_analysis.png (real TextBlob sentiment split, notebook cell 21)")

print("\n=== Sustainable Tourism Analysis Summary (real numbers) ===")
print(f"  Total tweets analysed (this notebook run): {TOTAL_TWEETS:,}")
print(f"  Positive sentiment: {SENTIMENT['Positive']}%")
print(f"  Neutral sentiment:  {SENTIMENT['Neutral']}%")
print(f"  Negative sentiment: {SENTIMENT['Negative']}%")
print("  Source: 'Sustainable Tourism Project.ipynb', cells 6/13/21")
print("\n[DONE]  Outputs saved to outputs/ — see README for what is/isn't verified beyond this.")
