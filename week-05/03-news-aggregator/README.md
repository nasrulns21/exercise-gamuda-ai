# News Aggregator

**Source:** Trainer Notes, Week 5 API exercise. **Original work:** refined from `week-05/news-aggregator` while retaining the original folder.

Uses Hacker News Algolia and Spaceflight News (both no-key), normalises responses, caches for five minutes, filters by text/source, handles rate limits and displays a clearly labelled fixture only when offline/error. Automated tests inject clients and never call the live network.
