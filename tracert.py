import subprocess
import platform
from concurrent.futures import ThreadPoolExecutor


def mTrace(host):
    systemOS = platform.system().lower()

    if systemOS == 'windows':
        command = ['tracert', '-h', '30', host]
    else:
        command = ['traceroute', '-m', '30', host]

    print(f"\n[Tracing route to {host}...]\n")

    try:
        # Live output - no stdout/stderr redirection
        response = subprocess.run(command)
        return response.returncode
    except Exception as e:
        print(f"Error tracing {host}: {e}")
        return None


def trace():
    target = input("Enter target host: ").strip()
    if not target:
        print("No target provided")
        return

    targets = target.split()  # Allow space-separated hosts
    print(f"\nScanning {len(targets)} target(s)...\n" + "-" * 30)

    with ThreadPoolExecutor(max_workers=min(len(targets), 5)) as executor:
        results = list(executor.map(mTrace, targets))

    print("\n" + "-" * 30)
    print("Scan complete.")
