# Wales Sustainable Tourism — Sentiment & NLP Analysis
[![UKRI Funded](https://img.shields.io/badge/Funded-UKRI-orange)](https://www.ukri.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-green)](https://python.org)
[![NLP](https://img.shields.io/badge/NLP-TextBlob-blue)]()
[![Tableau](https://img.shields.io/badge/Dashboard-Tableau%20Public-red)](https://public.tableau.com/app/profile/mac0173/vizzes)

## Business Problem

> *Welsh Government and tourism boards needed evidence-based insight into public perception of sustainable tourism to inform campaign strategy and policy.*

This UKRI-funded research project analyses public sentiment around sustainable tourism in Wales
from Twitter data. **What the notebook actually does, verified against its own executed
output:** loads a real 112,993-row tweet export (`tweets.xlsx`, dated roughly 2014–2023 based on
the `date` column — not 2010–2020), classifies each tweet's sentiment with TextBlob, and builds a
per-country choropleth map of sentiment. There is no topic/theme model (no LDA, no named themes
like "coastal access" or "heritage") and no campaign-timeline analysis anywhere in the notebook —
those claims, along with the ~800,000-tweet figure, could not be verified against this repo's
content and have been removed below until backed by a real, traceable analysis.

## Key Outputs

![Sentiment Analysis](outputs/01_sentiment_analysis.png)

*Real TextBlob sentiment split on the notebook's actual 112,993-row dataset — see
"Reproducing these numbers" below.*

**Tableau Dashboard:** [View on Tableau Public →](https://public.tableau.com/app/profile/mac0173/vizzes)
*(Not verified against this repo — check the dashboard directly for what it currently shows.)*

## Key Findings (real, from the notebook's own output)

| Metric | Value |
|--------|-------|
| Dataset volume (this notebook's loaded export) | 112,993 tweets |
| Date range observed in the `date` column | ~2014–2023 |
| Positive sentiment (TextBlob) | 52.58% |
| Neutral sentiment (TextBlob) | 39.70% |
| Negative sentiment (TextBlob) | 7.72% |
| Further analysis in notebook | Per-country sentiment choropleth map (cell 60) |

The README previously stated "Negative sentiment 39.7%" — that number is real but was
mislabelled; 39.7% is the *Neutral* share. Real negative share is 7.72%. The "top
positive/negative theme" and "+11% after government campaigns" figures have been removed — no
topic model or campaign-timeline analysis exists in this notebook to support them.

## NLP Pipeline (what's actually implemented)

| Stage | Method | Tool |
|-------|--------|------|
| Data loading | Read pre-collected tweet export | Pandas (`read_excel`/`read_csv`) |
| Preprocessing | URL/mention/punctuation/number stripping, stopword removal, stemming, lemmatisation | re, NLTK |
| Sentiment classification | TextBlob polarity → Positive/Neutral/Negative | TextBlob |
| Geographic breakdown | Per-country sentiment counts + choropleth | GeoPandas, Folium |

If VADER/LDA/Gensim topic modelling is added to the notebook later, update this table and the
Key Findings above to match — don't restate the old claims without a corresponding real cell.

## Quickstart

```bash
git clone https://github.com/Shreya-Macherla/Sustainable-Tourism
cd Sustainable-Tourism
pip install -r requirements.txt
python tourism_analysis.py                              # regenerates the real sentiment chart above
jupyter notebook "Sustainable Tourism Project.ipynb"   # full pipeline (source of the real numbers)
```

> Raw tweet data not included per Twitter's data redistribution policy. `tourism_analysis.py`
> renders the real percentages already computed in the notebook — it does not need the raw data
> to run.

## Reproducing these numbers

Every number in "Key Findings" above and in `outputs/01_sentiment_analysis.png` was copied
directly from `Sustainable Tourism Project.ipynb`'s own executed cells 6, 13, and 21 — open the
notebook and check those cells against the numbers here.

## Repository Structure

```
Sustainable-Tourism/
├── tourism_analysis.py                  # Re-plots the notebook's real sentiment split
├── Sustainable Tourism Project.ipynb    # Full research pipeline (source of truth)
├── outputs/
│   └── 01_sentiment_analysis.png        # Real sentiment breakdown, n=112,993
├── requirements.txt
└── README.md
```

## Tools

`Python 3.8` `NLTK` `TextBlob` `GeoPandas` `Folium` `Pandas` `Tableau` `Matplotlib`

## Funding

UKRI-funded research — Cardiff Metropolitan University.
