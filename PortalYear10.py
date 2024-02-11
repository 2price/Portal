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
                                                              
                              < Created By Cohen Turner >
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

def open_link(destination):
    # Define destinations and their corresponding links
    destinations = {
        "portal": "https://www.albertparkcollege.vic.edu.au/intranet/",
        "math": "https://sites.google.com/albertparkcollege.vic.edu.au/y10-foundation-maths?pli=1&authuser=3",
        "classroom": "https://classroom.google.com/u/3/h?pli=1",
        "law": "https://sites.google.com/albertparkcollege.vic.edu.au/10-international-economics-law/home?authuser=3",
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

    first_time = True

    while True:
        # Simulate loading for 1.5 seconds with a loading animation
        loading_animation(1.5, first_time)

        # Input destination from the user
        user_destination = input(f"\n{Fore.LIGHTYELLOW_EX}Enter destination (type 'exit' to quit): {Fore.RESET}").lower()

        if user_destination == 'exit':
            print("Exiting...")
            break

        # Open the link based on user's input
        open_link(user_destination)

        first_time = False
