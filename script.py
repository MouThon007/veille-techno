import feedparser
import requests

# Tes flux RSS illimités
FEEDS = [
    "https://www.cert.ssi.gouv.fr/feed/",
    "https://www.bleepingcomputer.com/feed/",
    "https://feeds.feedburner.com/TheHackersNews",
    "https://www.zataz.com/feed/",
    "https://www.undernews.fr/feed/",
    "https://rss.app/feeds/AiDBm87iUoOUUgke.xml",
    "https://rss.app/feeds/VyT5DXWV8PEXojkb.xml",
    "https://rss.app/feeds/b7CJIC1T9X8ttJwH.xml",
    "https://rss.app/feeds/edOIWpUf9QscWfpZ.xml",
    "https://rss.app/feeds/wqSrvca62DLhgS6m.xml",
    "https://www.lemondeinformatique.fr/flux-rss/rss.xml"
    
    
    
]

WEBHOOK_URL = https://discord.com/api/webhooks/1541207874062123109/aRQwtzP7BgIMl5BjPmm41xkKOM84d4cogaUWGH-qRniT66J8E2Kmn0yB7SB4xQ0Rx6sJ

for url in FEEDS:
    feed = feedparser.parse(url)
    for entry in feed.entries[:5]: # Regarde les 5 derniers articles
        title = entry.title
        link = entry.link
        # Filtre sur le mot ransomware (minuscules ou majuscules)
        if "ransomware" in title.lower() or "ransomware" in entry.get("summary", "").lower():
            msg = f"🚨 **Alerte Ransomware** : {title}\n{link}"
            requests.post(WEBHOOK_URL, json={"content": msg})