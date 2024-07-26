import pathlib
import json

def read_message(filename):
    """Reads different text file messages"""
    
    file_text = pathlib.Path(f'resources/{filename}.txt')
    contents = file_text.read_text()
    print(contents)
    

def read_keys():
    """Read credentials file and returns dictionary"""
    
    file = pathlib.Path("reddit_keys.json")
    contents = file.read_text()
    reddit_keys = json.loads(contents)
    return reddit_keys


def modify_keys(newkeys):
    """Write the keys in reddit_keysjson"""
    
    file = pathlib.Path("reddit_keys.json")
    contents = json.dumps(newkeys)
    file.write_text(contents)

    
def keyswitcher():
    """sets if there are existent keys or not"""
    
    file = pathlib.Path("keyconfig.json")
    contents = file.read_text()
    keystate = json.loads(contents)
    
    keystate["Existent_keys"] = 1;
    
    contents = json.dumps(keystate)
    file.write_text(contents)


def show_keys():
    """Shows the user the existent credentials"""
    
    reddit_keys = read_keys()
    for k,v in reddit_keys.items():
        print(f"{k}: {v}")
    print("\n")


def check_existing_keys():
    """Checks if the user has entered credentials before"""
    
    file = pathlib.Path("keyconfig.json")
    contents = file.read_text()
    keys = json.loads(contents)
    if keys['Existent_keys'] == 1:
        return True
    else:
        return False
     
     
def existent_keys_present():
    """Ask the user what to do with the already configured keys"""
    
    print("Existent Reddit Keys detected, do you want to use these?\n")
    show_keys()
    print("Type 'Y' to use saved keys or 'N' if you have new keys\n")
    
    user_input = input("Answer:")
    while(user_input.casefold() != "q"):
        if (user_input.casefold() == "y"):
            print("\nOkay, let's use these")
            break;
        
        elif (user_input.casefold() == "n"):
            print("\nOkay, let's set up new keys\n")
            add_new_keys()
            break;
        
        else:
            print("Wrong key. Try again Y/N or Q to quit")
            
        user_input = input("Answer:")     


def add_new_keys():
    """Helps the user set up the Reddit keys"""
    
    read_message('new_keys_message')
    
    reddit_keys = read_keys()
    print("\nPlease enter the Client ID")
    reddit_keys["client_id"] = input("Answer:")
    print(" ")
    print("Please enter the Client Secret")        
    reddit_keys["client_secret"] = input("Answer:")
    print(" ")
    print("Please enter the UserAgent")
    reddit_keys["user_agent"] = input("Answer:")
    print(" ")
    print("Please enter the account Username:")
    reddit_keys["username"] = input("Answer:")
    print(" ")
    print("Please enter the password:")
    reddit_keys["password"] = input("Answer:")
    
    modify_keys(reddit_keys)
    print("*******************")
    print("\nOkay, here are the keys you entered:\n")
    show_keys()
    print("Are these correct?. You can try to set them up again")
    print("Enter 'Y' to confirm the keys or 'N' to enter them again\n")
    user_input = input("Answer:")
    if (user_input.casefold() == "n"):
        print("\n Okay, let's try again...")
        add_new_keys()
    
    keyswitcher()
    


def replace_spaces_with_underscores(input_string):
    """
    I HATE POWERSHELL
    I HATE THE WINDOWS TASK SCHEDULER
    LITERALLY THE ANTICHRIST OF SOFTWARE
    """
    modified_string = input_string.replace(' ', '_')
    return modified_string