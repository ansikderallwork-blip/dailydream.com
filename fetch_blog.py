import feedparser
import json
import os

# আপনার ব্লগস্পট RSS ফিড ইউআরএল
BLOG_URL = "https://newdailydream1.blogspot.com/feeds/posts/default?alt=rss"

def fetch_all_posts():
    print("Fetching posts from Blogspot...")
    feed = feedparser.parse(BLOG_URL)
    posts_list = []

    for entry in feed.entries:
        post = {
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "content": entry.description
        }
        posts_list.append(post)

    # data ফোল্ডার না থাকলে তৈরি করবে
    os.makedirs('data', exist_ok=True)
    
    # data/posts.json ফাইলে সব ডাটা সেভ করবে
    with open('data/posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts_list, f, ensure_ascii=False, indent=2)
    
    print(f"Done! {len(posts_list)} posts cloned.")

if __name__ == "__main__":
    fetch_all_posts()
