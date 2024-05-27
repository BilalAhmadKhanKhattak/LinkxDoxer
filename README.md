![Image Alt Text](https://github.com/BilalAhmadKhanKhattak/LinkxDoxer/blob/main/Screenshot%20LinkxDoxer.png)

# LinkxDoxer

LinkxDoxer is a Python script designed to efficiently retrieve all links found directly under the webpage of a given URL. It is ideal for web developers, bug bounty hunters, and OSINT (Open-Source Intelligence) enthusiasts seeking to analyze links under a webpage and uncover valuable information(Expected In Ideal Cases)
## Features

- Retrieves all links found directly under the webpage of a given URL.
- Supports HTTP and HTTPS URLs.
- Customizable number of retries and delay between retries to handle network issues gracefully(Code Edit).
- Provides detailed error messages for better troubleshooting.

## Getting Started

1. **Installation:**
    - Clone this repository to your local machine.
    ```
    git clone https://github.com/BilalAhmadKhanKhattak/LinkxDoxer.git
    ```
2. **Prerequisites:**
    - Python 3
    - Install required dependencies using pip:
    ```
    pip install -r requirements.txt
    ```
3. **Usage:**
    - Run the script using Python:
    ```
    python LinkxDoxer.py
    ```
    - Enter the website URL when prompted and press Enter.
4. **Output:**
    - The script will display all the links found directly under the provided URL.

## Customization

You can customize the behavior of the script by modifying the following parameters in the script:
- `retries`: The number of times the script will retry retrieving the webpage in case of failures.
- `delay`: The delay (in seconds) between retry attempts.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue

## License

This project is licensed under the CC BY-NC 4.0 LEGAL CODE Attribution-NonCommercial 4.0 International License - see the LICENSE.txt file for details.

## Author

- [Bilal Ahmad Khan aka BILRED
- https://github.com/BilalAhmadKhanKhattak

