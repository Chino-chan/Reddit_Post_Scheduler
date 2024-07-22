# Reddit Post Scheduler ⏰
A command line tool made to set up and schedule Reddit Posts 

How to use this tool
--------------------

1) Install Python in your computer
2) Install PRAW library 
1) Get "keys" for the Reddit account you want to make a post from
2) Get to know your "keys" 
3) See the type of posts you can make



## Prerequisites

1. **Install Python**:

Make sure Python is installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).<br>
During installation, make sure to check the box that says "Add Python to PATH"

2. **Install PRAW Library**: 

This tool uses PRAW to interact with Reddit. After installing Python, open the "Windows Command Prompt"
Then run the following  command to install using pip:

   ```bash
   pip install praw



Getting your Reddit Keys
------------------------


- Go to the [Reddit Apps page](https://www.reddit.com/prefs/apps).
- Click on the "Create App" or "Create Another App" button.

<img src="https://i.imgur.com/K9JvUv2.jpeg"> 


- Fill out the required fields:
     - **Name**: Choose a name for your app (e.g., "MyRedditTool").
     - **App type**: Select "script" if you're using this tool for personal use.
     - **Description**: Provide a brief description of your app (optional).
     - **About url**: You can leave this blank.
     - **Redirect uri**: Enter `http://localhost:8080` (this can be any valid URL).
   - Click "Create app" to generate your API keys.

<img src="https://i.imgur.com/QuFBy0W.jpeg">

