import requests  # To handle HTTP requests
from bs4 import BeautifulSoup  # To parse HTML content and extract information from it
from urllib.parse import urljoin  # To parse and join URLs, ensuring that relative URLs are converted to absolute URLs.
from colorama import Fore, init  # For colors in the console output
import time  # To add delays Between Retries
import os  # for checking if file already exists

# Banner Things, You Can Ignore This Block:
init(autoreset=True)
banner = """
██╗     ██╗███╗   ██╗██╗  ██╗██╗  ██╗██████╗  ██████╗ ██╗  ██╗███████╗██████╗ 
██║     ██║████╗  ██║██║ ██╔╝╚██╗██╔╝██╔══██╗██╔═══██╗╚██╗██╔╝██╔════╝██╔══██╗
██║     ██║██╔██╗ ██║█████╔╝  ╚███╔╝ ██║  ██║██║   ██║ ╚███╔╝ █████╗  ██████╔╝
██║     ██║██║╚██╗██║██╔═██╗  ██╔██╗ ██║  ██║██║   ██║ ██╔██╗ ██╔══╝  ██╔══██╗
███████╗██║██║ ╚████║██║  ██╗██╔╝ ██╗██████╔╝╚██████╔╝██╔╝ ██╗███████╗██║  ██║
╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                            Version 1.2
                                                                                By MR. BILRED


Welcome to the LinkxDoxer! This script efficiently retrieves 
all links found directly under the webpage of a given URL. 
Ideal for web developers, bug bounty hunters, and OSINT (Open-Source Intelligence) enthusiasts 
seeking to analyze links under a webpage and uncover valuable information (EXPECTED IN IDEAL CASES)

Disclaimer = If You Do Any Malicious Activity, You, Yourself Are Responsible For It

Author = Bilal Ahmad Khan aka BILRED
Github = www.github.com/BilalAhmadKhanKhattak
Youtube = www.youtube.com/c/techambition [Maybe Not That Active Right Now]

Social media:
Facebook = Where people brag about their breakfast photos!
Instagram = Pics of cats being fabulous.
Twitter = Random thoughts at 3 AM.
LinkedIn = Pretending to be professional.
Snapchat = I'm Leaving This One For You, Hehe.

Just kidding, (Maybe Not)
----------------------------------------------------------------------------------
Hehe, I Got You, Below is The MAIN Thing
"""

print(Fore.LIGHTCYAN_EX + banner)


def get_all_links(url, retries=5, delay=1):
    for attempt in range(retries):
        try:
            # Make a request
            response = requests.get(url)

            # Check if response was successful
            if response.status_code != 200:
                print(f"Failed To Retrieve The Webpage, Status Code = {response.status_code} ")
                return []

            # Parse The Webpage Content:
            soup = BeautifulSoup(response.content, features='html.parser')

            # Now Finding All Anchor Tags(Shown below as a_tags) With href attribute
            links = []
            for a_tag in soup.find_all(name='a', href=True):
                # Convert Relative URLS To Absolute URLS
                absolute_url = urljoin(url, a_tag['href'])
                links.append(absolute_url)

            return links
        except requests.exceptions.MissingSchema:
            print("I Told You To Add https or http Before URL"
                  "for example: https://www.example.com")
            return []
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
        except Exception as e:
            print(f"Unknown Error Occurred: \n{e}")

        # Delay for all exceptions before the next attempt
        time.sleep(delay)

    print("Max Retries Exceeded")
    return []


if __name__ == "__main__":
    # Now Here Comes That PART
    website_url = input("Enter Website URL(also include http/https): ")
    links = get_all_links(website_url)
    print(f"Links Found On {website_url}:")

    if links:
        for i, link in enumerate(links, start=1):
            print(f"{i}. {link}")

    # Ask user if they want to save the links to a file 
    while True:
        save_to_file = input(Fore.LIGHTCYAN_EX + "Do you want to save to links to a file? (yes/no): ").strip().lower()
        if save_to_file in {'yes', 'no', ''}:
            break
        print(Fore.RED + "Invalid Input. Please enter 'yes' or 'no'.")

    if save_to_file == 'yes':
        filename = input(Fore.LIGHTCYAN_EX + "Enter the filename (with .txt extension): ").strip()
        if os.path.exists(filename):  # This snippet is to handle the situation if a filename already exists
            while True:
                overwrite = input(
                    f"The file '{filename}' already exists, Should I overwrite it? (yes/no): ").strip().lower()
                if overwrite in {'yes', 'no', }:
                    break
                print(Fore.RED + "Invalid Input, Please enter 'yes' or 'no'...")

            if overwrite != 'yes':
                print(Fore.RED + "File not saved.")
            else:
                with open(filename, 'w') as file:  # This 'w' means 'Write'
                    for i, link in enumerate(links, start=1):
                        file.write(f"{i}. {link}\n")
                    print(Fore.LIGHTGREEN_EX + f"Links Successfully Overwritten To '{filename}: ")

        else:
            with open(filename, 'w') as file:
                for i, link in enumerate(links, start=1):
                    file.write(f"{i}. {link}\n")
            print(Fore.LIGHTGREEN_EX + f"Links Successfully Saved To '{filename}': ")


    else:
        print("Something Happened!!!")

print("Press Any Key To Exit...")
input()
