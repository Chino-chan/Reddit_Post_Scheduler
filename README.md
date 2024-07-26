# Reddit Post Scheduler ⏰📆
A Windows command line tool made to set up and schedule Reddit Posts 

This tool is made for those that don't want to give their account to online services


How to use this tool
--------------------

1) Install Python & PRAW in your computer.
2) Get "keys" for the Reddit account you want to make a post from.
3) Know what each key means.
4) Run the program (With Admin Privileges)


IMPORTANT 😡
----------

- Once you download the folder place it where you won't move it, because when you schedule a post you can not move the folder to another directory.
This is because how it is programmed to be executed by the Windows Task Scheduler. 
if you move the folder, then the WTS will not find the files. You can move it again afterwards. 

- This will only work if, and only if, your computer is turned on at the moment you have
decided to schedule the post. This is because it has to be executed by Windows the Task Scheduler.
if your computer is turned off/sleeping then the WTS won't do it.



## Prerequisites

1. **Install Python**:

Make sure Python is installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).<br>
During installation, make sure to check the box that says "Add Python to PATH"

2. **Install PRAW Library**: 

This tool uses PRAW to interact with Reddit.<br>
After installing Python, open the "Windows Command Prompt"<br>

Then run the following  command to install using pip:

```bash
   pip install praw
```


Getting your Reddit Keys
------------------------


- Go to the [Reddit Apps page](https://www.reddit.com/prefs/apps).
- Click on the "Create App" or "Create Another App" button.


- Fill out the required fields:
     - **Name**: Choose a name for your app (e.g., "MyRedditTool").
     - **App type**: Select "script".
     - **Description**: You can leave this blank.
     - **About url**: You can leave this blank.
     - **Redirect uri**: Enter `http://localhost:8080` (this can be any valid URL).
   - Click "Create app" to generate your API keys.

<img src="https://i.imgur.com/6Ap6u6g.jpeg">


Knowing your Reddit Keys
------------------------

<img src="https://i.imgur.com/QgoDsNW.jpeg">


When you first run this program, it will ask you for your Reddit keys & Account info.<br>
The program will use this to interact with Reddit & automatically post.

- You will be asked for:
     - **Client ID**: It's the long code line under "personal use script".
     - **Client Secret**: It's the long code line next to "Secret".
     - **User Agent**: You can whatever in here (e.g., "MyRandomAgent44")
     - **Username**: The name of the Reddit Account that you want to make a post from.
     - **Password**: The password of the Reddit Account that you want to make a post from..

Both Username & Password have to be from the same account that you made the keys for.



Running the Program
------------------------

<img src="https://i.imgur.com/LE8gequ.jpeg">


You must run this program from the command line<br>
This program needs admin privileges to run because it interacts with Windows Task Scheduler<br>

- You do this by going to the program folder & opening the admin command line:
   - Clicking on "File"
   - "Open Windows Powershell"
   - "Open Windows Powershell as Admin"

Finally, running the program with the command

```bash
   python main.py
```

Then follow the steps in-program. 


Type of posts you can make
------------------------


- Text post 📃

Meaning, a post with a title and content body of only text<br>
You have to write the body of the post (not the title) in the "Text_Post" file<br>
Once you do this the program will make a copy and save it in "user_text"<br>

This is because you may want to schedule 2 text posts, you can safely erase the content<br>
of the "Text_Post" file after you have scheduled a post.<br>

Don't delete the "Text_Post" file or the file in "user_text" folder

------

- Image post 📷


You need to place the image you want to upload in the "reddit_images" folder<br>
It is recommended for the image name to be simple, like "cat.jpg"<br>
It is extremely important that you use the image extension, not only the name.<br>

If the image is named "cat" then see if it's "cat.jpg" or "cat.png"<br>
You need to write it fully Ex: "cat.jpg" for the program to recognize it.

Once you set up the scheduled post, don't remove the image from "reddit_images"


------

- Link Posts 🧲

This kind of posts are the ones you do when you want to submit a Youtube video<br>
a news article or etc. It has to be full complete link, such as<br> 

https://youtu.be/KGgtcz8u4rY?si=ICc3It7-PnQLx5WL

Don't submit it with quotemarks


How to cancel scheduled posts
------------------------

You can do this by either...

- Deleting the two files (python & .bat) that will be created after you schedule a task
The two files will have the same name as the title of the post you wanted to make.

- Deleting the scheduled task by opening the "Task Scheduler" in Windows
  The will be named after the title of the post

- Doing both 1&2

























