import requests
from bs4 import BeautifulSoup
import sys
import io

# Ensure UTF-8 output in Windows terminal
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def fetch_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.get_text(separator='\n').strip()[305:]
        else:
            print("Failed to fetch content.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def parse_data(raw_text):
    return raw_text.split('\n')

def parse_triplet_data(parsed_data_list):
    triplets = []
    for i in range(0, len(parsed_data_list), 3):
        x = int(parsed_data_list[i])
        char = parsed_data_list[i + 1]
        y = int(parsed_data_list[i + 2])
        triplets.append((x, y, char))
    return triplets

def grid_builder(triplet_data):
    max_x = max(x for x, y, char in triplet_data)
    max_y = max(y for x, y, char in triplet_data)
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y, char in triplet_data:
        grid[y][x] = char
    return grid

def print_grid_message(grid):
    for row in grid:
        print("".join(row))

# --- Main flow ---
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
raw_text = fetch_data(url)
if raw_text:
    parsed_lines = parse_data(raw_text)
    triplet_data = parse_triplet_data(parsed_lines)
    grid = grid_builder(triplet_data)
    print_grid_message(grid)
else:
    print("No data to display.")