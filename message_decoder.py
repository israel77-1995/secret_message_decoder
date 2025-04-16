import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    try:
        print(f"Fetching data from: {url}")  # Show the URL being passed

        # Send the GET request
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")  # Check the status code

        # If the request was successful, parse the HTML
        if response.status_code == 200:
            print("Parsing the HTML content...")
            soup = BeautifulSoup(response.text, 'html.parser')

            # You can print the whole parsed HTML to inspect it
            #print(f"This is the structure{soup.prettify()}")  # Uncomment this to see the structure

            # Extract the data you need from the HTML.
            # For example, if the characters are in a specific div, you could do something like:
            # data = soup.find_all("div", class_="some-class-name")

            # As an example, let's try printing all text inside <p> tags (just to inspect)
            paragraphs = soup.find_all('p')
            for p in paragraphs:
                print(p.get_text())

            return soup  # Or return the extracted content
        else:
            print(f"Failed to fetch content, status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Test the function
print(fetch_data("https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"))



def parse_data(data):
    # Check if the data is a list
    pass

