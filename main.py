import pathlib
import praw
import json
import os
import functionality
import scheduler


functionality.read_message('welcome')

#If no credentials are stored, then they will be set up
if functionality.check_existing_keys() == True:
    functionality.existent_keys_present()
else:
    print("No Reddit user keys detected. Let's configure them")
    functionality.add_new_keys()


#Once credentials are set up, the reddit post set-up begins
reddit_instance = scheduler.make_instance()
print("Now that we have keys, we can set up the actual post")
print("What subreddit would you like to schedule a post for?. Don't include 'r/'")
print("For example, if you want 'r/cats' then simply enter 'cats' (without quotemarks)")
choosen_subreddit = input("Answer:")
while(True):
    user_input = input(f"The choosen subreddit is: {choosen_subreddit}, is that correct? Y/N")
    if(user_input.casefold() == "y" ):
        break;
    choosen_subreddit = input("Let's try again, what subreddit would you like to schedule a post for?")

#Geting sub instance
subreddit_instance = reddit_instance.subreddit(choosen_subreddit)

## Deciding the post title
print("Enter the title of the reddit post to make:")
choosen_title = input("Answer:")

## Deciding the type of post, text/link or image
functionality.read_message("post_choices")
user_post_choice = input("")
while(True):
    if (user_post_choice.casefold == "A"):
        scheduler.text_post()
    elif (user_post_choice.casefold == "B"):
        scheduler.image_post()
    elif (user_post_choice.casefold == "C"):
        scheduler.link_post()
    else:
        print("Wrong letter, try again")



#Doing something to sub
#subreddit_instance.submit(title="test", url= "https://www.youtube.com/watch?v=FL-NhmFGQYw")
