import praw
import functionality
import pathlib
import textwrap
import os

def make_instance():
    reddit_keys = functionality.read_keys()
    
    reddit_instance = praw.Reddit(
        client_id = reddit_keys["client_id"],
        client_secret = reddit_keys["client_secret"],
        user_agent = reddit_keys["user_agent"],
        username = reddit_keys["username"],
        password  = reddit_keys["password"],
        )
    
    return reddit_instance


def create_post_file(type_post,title, subreddit, image ="", link=""):
    """
    This is the function that will finally finish setting up the post (not the schedule).
    after setting up either a text, link, or image post with their respective functions 
    this function will build the python file that will be executed by the scheduler
    """
    if type_post.casefold() == 'a':
        content = f"""
        import praw
        import functionality
        import scheduler
        import pathlib

        ##Creating Reddit Instance
        reddit_instance = scheduler.make_instance()

        ##Getting Subreddit Instance
        subreddit_instance = reddit_instance.subreddit("{subreddit}")
        
        ##Getting text to post
        file_text_post = pathlib.Path(f'user_text/{title}.txt')
        text_post = file_text_post.read_text()
        
        ##
        subreddit_instance.submit(title="{title}", selftext= text_post)
        """
        final_file_content = textwrap.dedent(content)
        file = pathlib.Path(f'{title}.py')
        file.write_text(final_file_content)
    
    if type_post.casefold() == 'b':
        content = f"""
        import praw
        import functionality
        import scheduler
        import pathlib

        ##Creating Reddit Instance
        reddit_instance = scheduler.make_instance()

        ##Getting Subreddit Instance
        subreddit_instance = reddit_instance.subreddit("{subreddit}")
        
        ##
        subreddit_instance.submit_image(title="{title}", image_path="reddit_images/{image}")
        """
        final_file_content = textwrap.dedent(content)
        file = pathlib.Path(f'{title}.py')
        file.write_text(final_file_content)
    
    if type_post.casefold() == 'c':
        content = f"""
        import praw
        import functionality
        import scheduler
        import pathlib

        ##Creating Reddit Instance
        reddit_instance = scheduler.make_instance()

        ##Getting Subreddit Instance
        subreddit_instance = reddit_instance.subreddit("{subreddit}")
        
        ##
        subreddit_instance.submit(title="{title}", url= "{link}")
        """
        final_file_content = textwrap.dedent(content)
        file = pathlib.Path(f'{title}.py')
        file.write_text(final_file_content)


def choose_subreddit():
    print("\nNow that we have keys, we can set up the actual post")
    print("What subreddit would you like to schedule a post for?. Don't include 'r/'")
    print("For example, if you want 'r/cats' then simply enter 'cats' (without quotemarks)")
    
    while(True):
        choosen_subreddit = input("\nAnswer:")
        if choosen_subreddit == "":
            print("\nYou can't leave that empty. Try again.")
            continue
        
        print(f"\nThe choosen subreddit is: {choosen_subreddit}, is that correct? Y/N")
        user_input = input(f"Answer:")
        if(user_input.casefold() == "y" ):
            break;
        
        print("\nLet's try again, what subreddit would you like to schedule a post for?")
    
    return choosen_subreddit


def choose_post_title():
    """A function that takes care of choosing the Reddit post title"""
    
    print("\nOkay, now enter the title of the reddit post you want to make:")
    while(True):
        choosen_title = input("Answer:")
        if choosen_title == "":
            print("\nYou can't leave that empty. Try again.")
            continue
        
        print(f"\nThe title will be : {choosen_title}, is that correct? Y/N")
        user_input = input(f"Answer:")
        if(user_input.casefold() == "y" ):
            return choosen_title
        
        print("\nLet's try again, what title would you like for the post?")


def set_text_post(title):
    """A function that will set up a text-based post"""

    functionality.read_message('postA')
    while(True):
        user_input = input("Answer:")
        if (user_input.casefold() == "y"):
            
            user_text_post = pathlib.Path(f'Text_Post.txt')
            text_post = user_text_post.read_text()
            
            copy_text_post = pathlib.Path(f'user_text/{title}.txt')
            copy_text_post.write_text(text_post)
            break
        else:
            print("Please enter Y when you have finished writing & saving the text file")


def set_image_post():
    functionality.read_message('postB')
    user_input = input("\nAnswer:")
    return user_input


def set_link_post():
    functionality.read_message('postC')
    user_input = input("\nAnswer:")
    return user_input


def send_link_post(subreddit_instance,title,url):
    subreddit_instance.submit(title="test", url= "https://www.youtube.com/watch?v=FL-NhmFGQYw")