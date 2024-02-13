import os
import subprocess
import time
import sys
from colorama import init, Fore

init(convert=True)

def tsu():
    print(f'''{Fore.LIGHTYELLOW_EX}
      
 ______   ______     ______     ______   ______     __        
/\  == \ /\  __ \   /\  == \   /\__  _\ /\  __ \   /\ \       
\ \  _-/ \ \ \/\ \  \ \  __<   \/_/\ \/ \ \  __ \  \ \ \____  
 \ \_\    \ \_____\  \ \_\ \_\    \ \_\  \ \_\ \_\  \ \_____\ 
  \/_/     \/_____/   \/_/ /_/     \/_/   \/_/\/_/   \/_____/ 
                                                              
                                   < Created By Cohen >
    < Year 10 Edition, you can view more versions @https://github.com/2price/Portal/tree/main >
                                                                                                              
{Fore.RESET}''')

def loading_animation(duration, first_time):
    for _ in range(int(duration * 5)):
        sys.stdout.write("\rLoading" + "." * (_ % 4) + "   ")
        sys.stdout.flush()
        time.sleep(0.2)
    if not first_time:
        sys.stdout.write("\r                ")
        sys.stdout.flush()

def open_link(destination, auth_user):
    # Define destinations and their corresponding links
    destinations = {
        "portal": f"https://www.albertparkcollege.vic.edu.au/intranet/?authuser={auth_user}",
        "math": f"https://sites.google.com/albertparkcollege.vic.edu.au/y10-foundation-maths?authuser={auth_user}",
        "classroom": f"https://classroom.google.com/u/{auth_user}/h?pli=1",
        "law": f"https://sites.google.com/albertparkcollege.vic.edu.au/10-international-economics-law/home?authuser={auth_user}",
        "posed": f"https://classroom.google.com/u/{auth_user}/c/NjQ5OTQ1MDc4MTE5",
        "english": f"https://sites.google.com/albertparkcollege.vic.edu.au/10-english/semester-1?authuser={auth_user}",
        "media": f"https://sites.google.com/albertparkcollege.vic.edu.au/create-10-media/home?authuser={auth_user}",
        "computing": f"https://classroom.google.com/u/{auth_user}/c/NjQ5OTQ0NTc5MDMx",
        "viscom": f"https://sites.google.com/albertparkcollege.vic.edu.au/create-10-visual-communication/home?authuser={auth_user}",
        "advanced math": f"https://sites.google.com/albertparkcollege.vic.edu.au/10-maths-advanced?authuser={auth_user}",
        "advanced english": f"https://sites.google.com/albertparkcollege.vic.edu.au/10-english-advanced?authuser={auth_user}",
        "vce english": f"https://sites.google.com/albertparkcollege.vic.edu.au/vce-english?authuser={auth_user}",
        "vce math": f"https://sites.google.com/albertparkcollege.vic.edu.au/vce-general-maths?authuser={auth_user}",
        # Add more destinations as needed
    }

    # Check if the input matches a predefined destination
    if destination in destinations:
        link = destinations[destination]
        print(f"Opening link: {link}")
        os.system(f"open {link}")
    else:
        print("Invalid destination.")


if __name__ == "__main__":
    # Display the text
    tsu()

    # Ask the user for their auth account
    auth_user = input(f"{Fore.LIGHTYELLOW_EX}Enter your auth account number: {Fore.RESET}")

    first_time = True

    while True:
        # Simulate loading for 1.5 seconds with a loading animation
        loading_animation(1.5, first_time)

        # Input destination from the user
        user_destination = input(f"\n{Fore.LIGHTYELLOW_EX}Enter destination (type 'exit' to quit): {Fore.RESET}").lower()

        if user_destination == 'exit':
            print("Exiting...")
            break

        # Open the link based on user's input and auth account
        open_link(user_destination, auth_user)

        first_time = False
