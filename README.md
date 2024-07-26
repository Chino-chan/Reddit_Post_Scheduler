# Reddit Post Scheduler ⏰📆
A command line tool made to set up and schedule Reddit Posts 

This tool is made for those that don't want to give their account to online services

How to use this tool
--------------------

1) Install Python in your computer.
2) Install PRAW. 
1) Get "keys" for the Reddit account you want to make a post from.
2) Know what each key means.
3) See the type of posts you can make.



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



The type of posts you can make
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






























