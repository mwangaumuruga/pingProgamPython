# Ping Script in Python

## Description

This script allows you to ping a specified domain or IP address to check network connectivity. It works on both Windows and Linux/macOS systems by automatically determining the correct ping command to use based on your operating system.

## Features

- Sends 4 ping requests to the specified host (e.g., `google.com`).
- Automatically adapts to Windows or Linux/macOS environments.
- Displays the ping results or error messages in the console.

## Requirements

- Python 3.x
- Internet connection (to ping external domains like `google.com`).

## How to Run

1. **Clone or download the script:**
    ```
    git clone https://github.com/mwangaumuruga/pingProgamPython
    ```

2. **Navigate to the directory containing the script:**
    ```
    cd ping-script
    ```

3. **Run the script:**
    ```
    python3 ping_script.py
    ```

4. **Change the host** (optional):
   - Open the script in a text editor and modify the `host` variable to the domain or IP address you'd like to ping.
   
   Example:
   ```python
   host = "example.com"  # Change 'example.com' to the host of your choice.
