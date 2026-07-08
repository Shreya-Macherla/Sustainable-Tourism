---
name: verify-narrative-against-code
description: Load before editing README.md or tourism_analysis.py, or any claim about sentiment findings, themes, or government-campaign response in this repo. Trigger on keywords — sentiment, UKRI, 800K tweets, themes, government campaign, coastal access.
---

# tourism_analysis.py always fabricates its tweet corpus — the README describes it as real research findings

`tourism_analysis.py` prints, every run: `"[DATA]  Generated {len(df):,} synthetic tweets
(2010–2020)"` from `generate_tweets(n=5000)` — this is honestly logged at runtime, which is
better than the HAR/Voice-Auth/Crypto cases. But the README doesn't carry that disclosure
forward. It states:

> This UKRI-funded research project analyses ~800,000 tweets from 2010–2020 to characterise
> public sentiment around sustainable tourism in Wales. The NLP pipeline identifies which themes
> (coastal access, heritage, sustainability) generate positive engagement vs. criticism — and
> tracks how sentiment shifted in response to government campaigns.

The `![Sentiment Analysis Dashboard](outputs/01_sentiment_analysis.png)` image embedded right
below that paragraph is generated from 5,000 synthetic tweets, not the 800K real dataset the
paragraph describes. A reader has no way to know, from the README alone, that the specific
themes/campaign-response claims illustrated in that image are demo output rather than the actual
UKRI research findings.

## Before touching this repo again

1. If the real 800K-tweet analysis exists (a notebook, a separate script, an actual research
   output from the UKRI project) — link to it and get the dashboard image from *that*, not from
   `tourism_analysis.py`'s synthetic run.
2. If it doesn't exist in this repo, the README needs a one-line disclosure directly under the
   embedded image: this chart is generated from a synthetic demo corpus illustrating the
   pipeline's mechanics, not the cited 800K-tweet study.
3. Don't remove the `[DATA] Generated ... synthetic tweets` print statement — that's the one
   honest signal currently in the pipeline; if anything, surface it in the README too.

## When NOT to use this skill

This repo has essentially no other code beyond the single analysis script (single-commit git
history, one script, one notebook-free structure) — there's no separate technical failure mode
here. This narrative/evidence gap is the one thing worth fixing.
