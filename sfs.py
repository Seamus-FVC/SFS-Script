# imports
import time
from tracert import *
from ping import *
import subprocess

# Declaring important variables
option = 0



def power_options():
    print("Power Options")
    choice = input("Please select 's' to shutdown, 'r' to restart your PC, or 'q' to abort to menu\n")
    if choice.lower() == "s":
        toggle = False
        subprocess.call(["shutdown", "/s", "/t", "30"])
        abort = input("Abort? (y/n)")
        if abort.lower() == "y":
            subprocess.call(["shutdown", "/a"])
        else:
            subprocess.call(["shutdown", "/p"])

    elif choice.lower() == "r":
        subprocess.call(["shutdown", "/p"])

    elif choice.lower() == "q":
        menu(menu_option)




def menu_option(option):
    if option == 1:
        mPing()
    elif option == 2:
        power_options()
    elif option == 3:
        trace()
    elif option == 4:
        print("Inconceivable")
    elif option == 5:
        count = 5
        for i in range(5):
            print(f"Self destruct in {count}")
            count = count - 1
            time.sleep(1)


def menu(menu_option):
    print(
        f"Hello, you can choose from the following options.\n1. Ping\n2. Laser Sharks\n3. Banish peasent of choice\n4. Nuke planet\n5. self destruct\n")
    option = int(input("Enter choice here: "))
    while (option < 1 and option > 5):
        option = int(input("Value not in bounds 1 and 5 please choose a number from one to 5: "))

    menu_option(option)


menu(menu_option)


