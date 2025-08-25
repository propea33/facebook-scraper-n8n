# main.py
from flask import Flask, request, jsonify
from facebook_scraper import get_posts

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Facebook Scraper API est en ligne !"

@app.route("/scrape", methods=["GET"])
def scrape():
    # Récupère la page à scraper (ex: conneriesqc)
    page = request.args.get("page")
    if not page:
        return jsonify({"error": "Merci de fournir ?page=nom_de_page"}), 400

    try:
        posts_data = []
        for post in get_posts(page, pages=1, options={"comments": False}):
            posts_data.append({
                "post_id": post.get("post_id"),
                "text": post.get("text"),
                "time": str(post.get("time")),
                "likes": post.get("likes"),
                "shares": post.get("shares"),
                "comments": post.get("comments"),
                "post_url": post.get("post_url")
            })
        return jsonify(posts_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
