from facebook_scraper import get_posts
import csv
from datetime import datetime

# Exemple : scraper les posts d'une page Facebook publique
def scrape_facebook(page="meme_page", max_posts=10):
    posts_data = []
    for post in get_posts(page, pages=1):  # pages=1 = une "page" de scroll
        posts_data.append({
            "time": post['time'],
            "text": post['text'],
            "likes": post['likes'],
            "comments": post['comments'],
            "shares": post['shares']
        })
        if len(posts_data) >= max_posts:
            break

    # Sauvegarde CSV
    filename = f"output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=posts_data[0].keys())
        writer.writeheader()
        writer.writerows(posts_data)

    print(f"✅ Données sauvegardées dans {filename}")

if __name__ == "__main__":
    scrape_facebook("conneriesqc", 10)
