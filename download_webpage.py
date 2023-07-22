import os
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def sanitize_filename(filename):
    # Remove special characters from the filename using regular expressions
    return re.sub(r'[^\w\-_.]', '', filename)

def download_web_page(url, local_directory):
    try:
        # Check if the URL is valid
        response = requests.head(url)
        response.raise_for_status()  # Raise an exception for invalid URLs
    except requests.RequestException as e:
        print(f"Error: Invalid URL or cannot connect to the server.\n{e}")
        return

    try:
        # Send a GET request to fetch the web page
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for unsuccessful requests

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Create the local directory if it doesn't exist
        if not os.path.exists(local_directory):
            os.makedirs(local_directory)

        # Download and save embedded images
        for img_tag in soup.find_all('img'):
            try:
                img_url = img_tag['src']
                img_url = urljoin(url, img_url)  # Make sure the URL is absolute
                img_name = os.path.basename(img_url)

                # Sanitize the image name to remove invalid characters
                img_name = sanitize_filename(img_name)

                local_img_path = os.path.join(local_directory, img_name)

                img_response = requests.get(img_url)
                img_response.raise_for_status()  # Raise an exception for unsuccessful image requests

                with open(local_img_path, 'wb') as f:
                    f.write(img_response.content)
                print(f"Image {img_name} downloaded and saved to {local_img_path}")
            except requests.RequestException as e:
                print(f"Error downloading image {img_name}: {e}")

        # Save the content of the web page to a local file
        local_file_path = os.path.join(local_directory, "index.html")
        with open(local_file_path, 'wb') as f:
            f.write(response.content)
        print(f"Web page downloaded and saved to {local_file_path}")
    except requests.RequestException as e:
        print(f"Error downloading the web page: {e}")

# Example usage with command-line arguments
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python download_web_page.py [url] [local_directory]")
    else:
        url_to_download = sys.argv[1]
        local_directory = sys.argv[2]

        download_web_page(url_to_download, local_directory)
