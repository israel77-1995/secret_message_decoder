import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    try:
        print(f"Fetching data from: {url}")

        # Make the HTTP request
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            print("Parsing the HTML content...")

            # Parse the HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # ✅ Return only the visible text (removes HTML/JS)
            clean_text = soup.get_text(separator='\n').strip() 
            return clean_text[301:]

        else:
            print("Failed to fetch content.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Test the function
print(fetch_data("https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"))


def parse_data(data):
  
    data_lines = data.splitlines()

    print(f"Number of lines in data: {len(data_lines)}")
    print(data_lines)
    return data_lines
# Test the function
url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
raw_text = fetch_data(url)
parsed_lines = parse_data(raw_text)
