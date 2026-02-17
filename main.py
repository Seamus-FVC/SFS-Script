#imports
import time
import sys
import platform
import subprocess
from concurrent.futures import ThreadPoolExecutor



#Declaring important variables
option = 0



def ping(host):
    systemOS = platform.system().lower()
    param = "-n" if systemOS == 'windows' else '-c'
    command = ['ping', param, '1', '-w' if systemOS != 'windows' else '-w', '1000', host]

    try:
        response = subprocess.run(
            command, stdout= subprocess.DEVNULL, stderr= subprocess.DEVNULL
        )
        status = " Online " if response.returncode == 0 else " Offline "
        return f"{host:20} : {status}"
    except Exception:
        return f"{host:20} : Error"

def mPing():
    userInput = input("Enter targets chud - seperate with a comma")
    targets = [t.strip() for t in userInput.split(',') if t.strip()]
    if not targets:
        print("No matching victims chudette")
        return
    print(f"\nScanning {len(targets)} targets...\n" + "-"*30)

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(ping, targets))
    for result in results:
        print(result)

def power_options():
    print("Power Options")
    choice = input("Please select 's' to shutdown, 'r' to restart your PC, or 'q' to abort to menu\n")
    if choice.lower() == "s":
        subprocess.call(["shutdown", "/p"])

    elif choice.lower() == "r":
        subprocess.call(["shutdown", "/p"])
    
    elif choice.lower() == "q":
        menu(menu_option)
    


def menu_option(option, mPing):
    match option:
        case 1:
            mPing()
        case 2:
            power_options()
        case 3:
            print("Jim has been banished")
        case 4:
            print("Inconceivable")
        case 5:
            count = 5
            for i in range(5):
                print(f"Self destruct in {count}")
                count = count-1
                time.sleep(1)

def menu(menu_option):
    print(f"Hello, you can choose from the following options.\n1. Ping\n2. Laser Sharks\n3. Banish peasent of choice\n4. Nuke planet\n5. self destruct\n")
    option = int(input("Enter choice here: "))
    while(option < 1 and option > 5):
        option = int(input("Value not in bounds 1 and 5 please choose a number from one to 5: "))

    menu_option(option, mPing)
   

menu(menu_option)


    


