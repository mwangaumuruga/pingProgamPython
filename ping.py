# This script uses the subprocess module to run the ping command on a specified host.
# It returns the output of the ping command, which includes the number of successful ping responses.
#!/usr/bin/python3
import os       # Provides a way to interact with the operating system
import platform # Used to get information about the operating system (OS)
import subprocess  # Allows running external commands (e.g., ping)

def ping(host):
    # Determine the command parameter based on the operating system.
    # 'platform.system()' tells us the type of OS (e.g., Windows, Linux, MacOS).
    # On Windows, the ping command uses the '-n' flag, while Linux/Mac use '-c' to define the number of ping requests.
    param = "-n" if platform.system().lower() == "windows" else "-c"

    # Build the ping command: it's a list of arguments
    # Example for Linux: ['ping', '-c', '4', 'google.com']
    # Example for Windows: ['ping', '-n', '4', 'google.com']
    command = ["ping", param, "4", host]

    # Execute the command using subprocess.run(). It runs the ping command as if you typed it into the terminal.
    # 'stdout' captures the output of the command (successful ping responses).
    # 'stderr' captures errors or warnings.
    # 'text=True' makes sure the output is in string format rather than bytes.
    return subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# This section only runs if the script is executed directly (not imported as a module in another script).
if __name__ == "__main__":
    host = "google.com"  # Host to ping. You can replace this with any domain or IP address.
    
    # Call the ping function to ping the specified host.
    response = ping(host)

    # Check if the ping command was successful.
    if response.returncode == 0:
        print(f"Ping to {host} was successful.")
        print(response.stdout)  # Print the details of the successful ping.
    else:
        print(f"Ping to {host} failed.")
        print(response.stderr)  # Print the error message if ping failed.
