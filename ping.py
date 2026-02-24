import sys
import platform
import subprocess
from concurrent.futures import ThreadPoolExecutor

def ping(host):
    systemOS = platform.system().lower()
    param = "-n" if systemOS == 'windows' else '-c'
    command = ['ping', param, '1', '-w' if systemOS != 'windows' else '-w', '1000', host]

    try:
        response = subprocess.run(
            command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
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
    print(f"\nScanning {len(targets)} targets...\n" + "-" * 30)

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(ping, targets))
    for result in results:
        print(result)
