#!/usr/bin/python3
import os
import platform
import subprocess

def ping(host):
    # Determine the command based on the operating system
    param = "-n" if platform.system().lower() == "windows" else "-c"

    # Build the ping command
    command = ["ping", param, "4", host]

    # Execute the command and get the output
    return subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Example usage
if __name__ == "__main__":
    host = "google.com"  # You can replace this with any IP or domain
    response = ping(host)

    if response.returncode == 0:
        print(f"Ping to {host} was successful.")
        print(response.stdout)
    else:
        print(f"Ping to {host} failed.")
        print(response.stderr)
