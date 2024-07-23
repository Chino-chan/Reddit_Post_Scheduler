import praw
import functionality
import pathlib
import textwrap
import os

def make_instance():
    """
    This creates the basic Reddit instance from the praw module
    For that it needs to read the Reddit account keys stored in reddit_keys.json
    """
    reddit_keys = functionality.read_keys()
    
    reddit_instance = praw.Reddit(
        client_id = reddit_keys["client_id"],
        client_secret = reddit_keys["client_secret"],
        user_agent = reddit_keys["user_agent"],
        username = reddit_keys["username"],
        password  = reddit_keys["password"],
        )
    
    return reddit_instance


def create_post_file(type_post,title, subreddit, fixed_file_title, image ="", link="", ):
    """
    This is the function that, with all details gathered, will set up the python file (not the scheduler).
    The python file it sets up will be the one that the Windows Task Scheduler has to execute. 
    This python file will be the one that interacts with Reddit API through the PRAW library
    
    In the case of a text post (A) it will read the text it previously copied into "user_text/..."
    In the case of an image post (B) it will look for the image name in "reddit_images/..."
    In the case of a link post (C) it will get passed the link and place it directly.
    
    If this Python file is executed, it will make the Reddit post.
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
        file_text_post = pathlib.Path(f'user_text/{fixed_file_title}.txt')
        text_post = file_text_post.read_text()
        
        ##
        subreddit_instance.submit(title="{title}", selftext= text_post)
        """
        final_file_content = textwrap.dedent(content)
        file = pathlib.Path(f'{fixed_file_title}.py')
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
        file = pathlib.Path(f'{fixed_file_title}.py')
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
        file = pathlib.Path(f'{fixed_file_title}.py')
        file.write_text(final_file_content)


def create_batch_file(title):
    content = f"""
    @echo off
    rem Change directory to the directory of this batch file
    cd /d "%~dp0"
    python {title}.py
    pause
    """
    
    final_file_content = textwrap.dedent(content)
    file = pathlib.Path(f'{title}.bat')
    file.write_text(final_file_content)


def choose_subreddit():
    """
    Sets up the subreddit to make a post for by asking the user
    Returns the choosen subreddit once the user confirms the subreddit
    """
    
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
            return choosen_subreddit
        
        print("\nLet's try again, what subreddit would you like to schedule a post for?")
    
    


def choose_post_title():
    """
    Sets up the title of the post the user wants to make by asking for it.
    Returns the title once the user has confirmed the title
    """
    
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


def set_text_post(fixed_file_title):
    """
    This will help set up a text based post
    Once the user writes the body of the post in the "Text_Post.txt" file
    It will be copied to "user_text" folder
    The text file will be named like the title of the Reddit Post is linked with
    """

    functionality.read_message('postA')
    while(True):
        user_input = input("Answer:")
        if (user_input.casefold() == "y"):
            
            user_text_post = pathlib.Path(f'Text_Post.txt')
            text_post = user_text_post.read_text()
            
            copy_text_post = pathlib.Path(f'user_text/{fixed_file_title}.txt')
            copy_text_post.write_text(text_post)
            break
        else:
            print("Please enter Y when you have finished writing & saving the text file")


def set_image_post():
    """
    Helps set an image type of post by prompting the user for the complete name of the image
    The image will have to be complete eg: "Dog.jpg" "Cat.png" this will be returned
    The user will have to put the image in the "reddit_images" folder later
    """
    
    functionality.read_message('postB')
    user_input = input("\nAnswer:")
    return user_input


def set_link_post():
    """
    Helps set a post with a link (news/youtube) by prompting the user for the link
    The complete link eg: "https://www.youtube.com/watch?v=KGgtcz8u4rY" will be returned
    """
    functionality.read_message('postC')
    user_input = input("\nAnswer:")
    return user_input


