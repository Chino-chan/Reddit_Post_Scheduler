import praw
import functionality
import pathlib

def make_instance():
    reddit_keys = functionality.read_keys()
    
    reddit_instance = praw.Reddit(
        client_id = reddit_keys["client_id"],
        client_secret = reddit_keys["client_secret"],
        user_agent = reddit_keys["user_agent"],
        sername = reddit_keys["username"],
        password  = reddit_keys["password"],
        )

def text_post():
    functionality.read_message('postA')
    user_input = input("Answer: ")
    if (user_input.casefold == "y"):
        file_text = pathlib.Path('Text_Post.txt')
        contents = file_text.read_text()

def image_post():
    pass

def link_post():
    pass

