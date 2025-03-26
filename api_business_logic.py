from api_client import APIclient
import logging
from tabulate import tabulate

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,  # or DEBUG, WARNING, ERROR
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)


"""
Manager class handles communication with the external API and wraps
business logic such as creating, fetching, updating, and deleting issues.
"""

class Manager:
    def __init__(self, user_name, password):
        self.client = APIclient(user_name, password)
        try:
            user_info = self.client.connectivity_test()
            self.token = user_info["accessToken"]
            logging.info(f"Connected to {user_name} successfully")
        except Exception as e:
            logging.error(f"Failed to connect to {user_name}, please try again.: {e}")
            raise(e)

    def get_user_details(self):
        try:
            user_info = self.client.connectivity_test()
            data = {"id": user_info["id"], "user_name": user_info["username"], "email": user_info["email"], "first_name": user_info["firstName"], "last_name": user_info["lastName"], "gender": user_info["gender"], "image": user_info["image"]}
            table = tabulate(data.items(), headers=["Field", "Value"], tablefmt="fancy_grid")
            print(table)
        except Exception as e:
            logging.error(f"Failed to fetch user details: {e}")
            raise(e)
        
    def get_posts(self, limit):
        try:
            response = self.client.get(endpoint=f"/posts?limit={limit}")
            posts = response.get("posts", [])
            posts_to_display = []
            for post in posts:
                posts_to_display.append({"id": post["id"], "title": post["title"], "tags": post["tags"], "likes 👍🏻": post["reactions"]["likes"], "dislikes 👎🏻": post["reactions"]["dislikes"], "views": post["views"]})
            table = tabulate(posts_to_display, headers="keys", tablefmt="fancy_grid")
            print(table)
        except Exception as e:
            logging.error(f"Failed to fetch posts: {e}")
            raise(e)
    
    def get_posts_and_comments(self, limit):
        try:
            response = self.client.get(endpoint=f"/posts?limit={limit}")
            posts = response.get("posts", [])
            posts_with_comments = []
            for post in posts:
                post_id = post["id"]
                post_title = post["title"]
                comments = self.client.get(endpoint=f"/posts/{post_id}/comments")
                posts_with_comments.append({"post_id": post, "comments": comments})
                display = []
                for comment in comments["comments"]:
                    id = comment["id"]
                    body = comment["body"]
                    likes = comment["likes"]
                    display.append({"id": id, "body": body, "likes 👍🏻": likes})
                print(f"\n📨 Comments for Post: {post_title}")
                if display:
                    table = tabulate(display, headers="keys", tablefmt="fancy_grid")
                    print(table)
                else:
                    print("No comments found.")
                    

        except Exception as e:
            logging.error(f"Failed to fetch posts: {e}")
            raise(e)
