import pathlib
import praw
import json
import os
import functionality
import scheduler



#When program is run, first the welcome message will be displayed, then
#the program will look for existent reddit keys, if it finds some, then
#it will ask the user if it wants to generate new ones or use the ones found.
functionality.read_message('welcome')

if functionality.check_existing_keys() == True:
    functionality.existent_keys_present()
else:
    print("No Reddit user keys detected. Let's configure them")
    functionality.add_new_keys()


#Once credentials are set up, the reddit post set-up begins
#First we make an instance of Reddit, then we ask the user for the subreddit they want
#Finally, we make an instance of the subreddit the user has choosen
#reddit_instance = scheduler.make_instance()
choosen_subreddit = scheduler.choose_subreddit()
#subreddit_instance = reddit_instance.subreddit(choosen_subreddit)

# Deciding the post title
post_choosen_title = scheduler.choose_post_title()

# Deciding the type of post, text/link or image
print("\n***********************************")
print("\nOkay, now that we have the subreddit & title, what kind of post do you want to make?\n")
functionality.read_message("post_choices")

valid_choices = ('a','b','c')
while(True):
    user_post_choice = input("Answer:")
    if (user_post_choice.casefold() in valid_choices):
        break
    else:
        print("Wrong input, please try again\n")
        print("Wrong letter, try again")

# Setting up the post content according to choice
# Case A sets the text post, doesn't need to return anything
# Case B sets the image post, needs to return the name of the image
# Case C sets the link post, needs to return the link
if (user_post_choice.casefold() == "a"):
    scheduler.set_text_post(title = post_choosen_title)   
elif (user_post_choice.casefold() == "b"):
    image_name = scheduler.set_image_post()    
elif (user_post_choice.casefold() == "c"):
    user_link = scheduler.set_link_post()
    
# Finally creating the Python file that will make the post using the keys & WRAP library
if user_post_choice.casefold() == "a":
    scheduler.create_post_file(type_post = user_post_choice, title = post_choosen_title, subreddit = choosen_subreddit )
if user_post_choice.casefold() == "b":
    scheduler.create_post_file( type_post = user_post_choice, title = post_choosen_title, subreddit = choosen_subreddit, image = image_name)
if user_post_choice.casefold() == "c":
    scheduler.create_post_file(type_post = user_post_choice, title = post_choosen_title, subreddit = choosen_subreddit, link= user_link )