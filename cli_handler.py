from api_business_logic import Manager
import os
import questionary
from colorama import Fore, Style, init


init(autoreset=True)

def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
def welcome_message():
    print("🚀 Welcome to the Anecdotes Plugin – collect user info, posts, and comments from the DummyJSON API.")


def setup_manager():
    while True:
        try:
            user_name = questionary.text("Please enter the user name:").ask()
            password = questionary.text("Please enter the user password:").ask()
            manager = Manager(user_name, password)  

            if manager:
                return manager
        except Exception as e:
            action = questionary.select("Try again?", choices = ["Yes", "No"]).ask()
            if action == "Yes":
                continue
            else:
                print("Thank you, Goodbye👋!")
                return None
                
def main_menu(manager: Manager):
    while True:
        try:
            action = questionary.select(
                "What would you like to do?",
                choices = ["E1 - Collect user details", "E2 - Collect a list of 60 posts in the system", "E3 - Collect a list of 60 posts, including each post’s comments", "Exit 🚪"]
            ).ask()

            if action == "E1 - Collect user details":
                manager.get_user_details()
            elif action == "E2 - Collect a list of 60 posts in the system":
                manager.get_posts(limit=60)
            elif action == "E3 - Collect a list of 60 posts, including each post’s comments":
                manager.get_posts_and_comments(limit=60)
            elif action == "Exit 🚪":
                print(Fore.MAGENTA + "Thank you 🚀\nGoodbye! 👋" + Style.RESET_ALL)
                break


        except Exception as e:
            print(Fore.RED + "Oops! Something went wrong, Please try again." + Style.RESET_ALL)