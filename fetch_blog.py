import feedparser
import json
import os

# আপনার ব্লগস্পট RSS ফিড ইউআরএল
BLOG_URL = "https://newdailydream1.blogspot.com/feeds/posts/default?alt=rss"

def fetch_latest_post():
    feed = feedparser.parse(BLOG_URL)
    if feed.entries:
        latest_post = feed.entries[0]
        
        # ডাটা ফরম্যাট তৈরি
        data = {
            "title": "DailyDream",
            "headline": latest_post.title,
            "description": latest_post.description[:500] + "..." # প্রথম ৫০০ অক্ষর
        }
        
        # data/home.json ফাইলে সেভ করা
        os.makedirs('data', exist_ok=True)
        with open('data/home.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_content_type=False, indent=2)
        print("Latest post cloned successfully!")

if __name__ == "__main__":
    fetch_latest_post
  ()
