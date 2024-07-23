import pathlib
import praw
import json
import os
import subprocess
import functionality
import scheduler
from datetime import datetime


#When program is run, first the welcome message will be displayed, then
#the program will look for existent reddit keys, if it finds some, then
#it will ask the user if it wants to generate new ones or use the ones found.
functionality.read_message('welcome')

if functionality.check_existing_keys() == True:
    functionality.existent_keys_present()
else:
    print("No Reddit user keys detected. Let's configure them")
    functionality.add_new_keys()


#Once credentials are set up, the actual reddit post set-up begins
#First we ask the user for the subreddit they want to schedule a post for
#Then we ask for the title of that post
choosen_subreddit = scheduler.choose_subreddit()
post_choosen_title = scheduler.choose_post_title()
no_whitespaces_file_title = functionality.replace_spaces_with_underscores(post_choosen_title)

# Now we let the user decide what kind of post they want
# If they want to post a text based post, a picture or a link (= news/video)
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

# This will set up the post details according to the type of post the user has choosen
# Case A sets the text post, doesn't return anything
# Case B sets the image post, returns the name of the image the user wants to post
# Case C sets the link post, returns the link the user wants to post
if (user_post_choice.casefold() == "a"):
    scheduler.set_text_post(fixed_file_title = no_whitespaces_file_title)   
elif (user_post_choice.casefold() == "b"):
    image_name = scheduler.set_image_post()    
elif (user_post_choice.casefold() == "c"):
    user_link = scheduler.set_link_post()
    
# When all details for the type of post are gathered in the previou step
# Now creation of the Python file that will make the post using the keys & WRAP library is done
if user_post_choice.casefold() == "a":
    scheduler.create_post_file(type_post = user_post_choice, fixed_file_title= no_whitespaces_file_title,title = post_choosen_title, subreddit = choosen_subreddit )
if user_post_choice.casefold() == "b":
    scheduler.create_post_file( type_post = user_post_choice, fixed_file_title= no_whitespaces_file_title, title = post_choosen_title, subreddit = choosen_subreddit, image = image_name)
if user_post_choice.casefold() == "c":
    scheduler.create_post_file(type_post = user_post_choice, fixed_file_title= no_whitespaces_file_title,title = post_choosen_title, subreddit = choosen_subreddit, link= user_link )
    
    
    
# Now that the Python file that will create the post is done,
# The Windows Task Scheduler needs to be set up so it can eventually execute it.
# We now ask the user when does it want to make the post and so on.
print("\n")
functionality.read_message("scheduler")

day = input("Enter the day (DD):")
month = input("Enter the month (MM):")
year = input("Enter the year (YYYY):")
time = input("Enter the time (HH:MM in 24-hour format):")

try:
    specific_date_time = datetime.strptime(f"{year}-{month}-{day}T{time}", "%Y-%m-%dT%H:%M")
    specific_date_time_str = specific_date_time.strftime("%Y-%m-%dT%H:%M:%S")
except ValueError as e:
    print(f"Error: {e}")
    exit(1)




# Begin construction of Powershell task scheduler command
#
# File path builder. 
# Necessary to retrieve the full location of the Python file
# current directory of the running Python script:
script_dir = os.path.dirname(os.path.abspath(__file__))
python_post_file = os.path.join(script_dir, f'{no_whitespaces_file_title}.py')
bat_post_file = os.path.join(script_dir, f'{no_whitespaces_file_title}.bat')

# Create the batch file that will execute the Python file
scheduler.create_batch_file(no_whitespaces_file_title)

#print("*******")
#print(python_post_file)
#escaped_script_path = python_post_file.replace("\\", "\\\\")
#print("*******")
#print(escaped_script_path)
#cript_path = rf"{python_post_file}"
#print("*******")
#print(cript_path)




# Format specific_date_time for PowerShell schtasks command
powershell_date_format = specific_date_time.strftime("%m/%d/%Y")
powershell_time_format = specific_date_time.strftime("%H:%M")


# Construct PowerShell command
powershell_command = f'schtasks /Create /TN "{no_whitespaces_file_title}" /SC ONCE /ST {powershell_time_format} /SD {powershell_date_format} /TR "{bat_post_file}" /RL HIGHEST'
subprocess.run(["powershell", "-Command", powershell_command])




#powershell_command = f'schtasks /Create /TN "RunSecondFileTask" /SC ONCE /ST {specific_date_time_str} /SD {specific_date_time_str} /TR "{bat_post_file}"'




#powershell_command = f"""
#$action = New-ScheduledTaskAction -Execute "{bat_post_file}"
#$trigger = New-ScheduledTaskTrigger -Once -At "{specific_date_time_str}"
#$principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount -RunLevel Highest
#$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
#Register-ScheduledTask -Action $action -Trigger $trigger -Principal $principal -Settings $settings -TaskName "{post_choosen_title}" -Description "This task runs the {post_choosen_title} on {specific_date_time_str}"
#"""

#result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)

# Print the output of the PowerShell command
#print(result.stdout)
#if result.returncode != 0:
#    print(f"Error: {result.stderr}")