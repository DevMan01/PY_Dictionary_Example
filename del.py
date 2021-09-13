from os import system, name # Import libraries to manage the system console.
import time #Import the time library for utility.
import logging # Import logging for debugging and troubleshooting.

# Variables
college_football = {
                    "Utes" : "Swoop",
                    "Ohio State" : "Buckeyes",
                    "Michigan" : "Wolverines",
                    "Oregan State" : "Ducks",
                    "Boise State" : "Broncos"}

# Create a fucntion that clears the terminal screen.
def clear():
    if name == "nt":
        logging.debug("Attempting to clear a Windows console.")
        _ = system("cls")
    else:
        logging.debug("Attempting to clear a MacOS terminal.")
        _ = system("clear")

# Create a function to load the dictionary data type.
## to-do: switch to importing from a file.
## to-do: make this dynamic so it can imnport anything into a dictionary.
def load_college_team_dictionary():
    logging.debug("Attempting to load the college team dictionary.")

    logging.debug("Load successful.")
    print_college_football_dictionary()

# Create a function that prints the contents of the dictionary.
## to-do: make this dynamic so that it could print the contents of any dictionary.
def print_college_football_dictionary():
    logging.debug("Attempting to print out the content of the dictionary.")
    for key, value in college_football.items():
        print(key, ' : ', value)
    logging.debug("Print successful.")

# A function that removes values from the dictionary
def remove_state():
    clear()
    print_college_football_dictionary()

    try:
        user_removal = str(input("\nWhich state would you like to remove?\n"))
        if user_removal in college_football:
            logging.debug("Attempting to remove a state from the dictionary.")
            user_removal= college_football.pop(user_removal, None)
            logging.debug("Removal successful.")
        else:
            raise NameError
    except(NameError):
        logging.warning("An exception has occurred. User unexpected value.")
        print("You've selected an invalid option, try again.")
        time.sleep(1)
        remove_state()

    main_menu()

 # A function that removes values from the dictionary
def add_state():
    clear()
    print_college_football_dictionary()
    state= input("What is the name of the state you'd like to add?\n")
    team_name= input("What is the team name?")
    logging.debug("Attempting to add a state to the dictionary.")
    college_football[state] = team_name
    logging.debug("Addition successful.")
    main_menu()

# A function to run the main menu.
def main_menu():
    clear()
    acceptable_input = ("q", "r", "a", "p")
    while True:
        try:
            user_input = input("What would you like to do?\n" +
                           "Options: \n" +
                           "'Q' To quit program. \n" +
                           "'R' To remove a team. \n" +
                           "'A' to add a new team. \n" +
                           "'P' to show all teams. \n")

            if user_input not in acceptable_input:
                raise NameError
            elif user_input == "r":
                remove_state()
            elif user_input == "a":
                add_state()
            elif user_input == "p":
                print()
                print_college_football_dictionary()
                print("\nWaiting 3 seconds...")
                time.sleep(3)
                main_menu()
            elif user_input == "q":
                print('Exiting the program')
                quit()

        except(NameError):
            logging.warning("An exception has occurred. User unexpected value.")
            print("You've selected an invalid option, try again.")
            time.sleep(1)
            main_menu()
        except(KeyboardInterrupt):
            print("\nQuitting.")
            logging.info("User has quit the app through keyboard interrupt.")
            quit()



#-------------------------------------------------------------------------------
# Main execution here.
#-------------------------------------------------------------------------------

# Set up logging config, incase I need to debug later.
logging.basicConfig(filename='runtime.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S')

load_college_team_dictionary()
main_menu()
