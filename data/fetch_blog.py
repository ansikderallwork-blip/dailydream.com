import feedparser
import json
import os

BLOG_URL = "https://newdailydream1.blogspot.com/feeds/posts/default?alt=rss"

def fetch_all_posts():
    feed = feedparser.parse(BLOG_URL)
    posts_list = []

    for entry in feed.entries:
        post = {
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "content": entry.description # এখানে পুরো পোস্টের বডি আসবে
        }
        posts_list.append(post)

    # data ফোল্ডার তৈরি এবং সেভ করা
    os.makedirs('data', exist_ok=True)
    with open('data/posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts_list, f, ensure_ascii=False, indent=2)
    print(f"Successfully cloned {len(posts_list)} posts!")

if __name__ == "__main__":
    fetch_all_posts()
