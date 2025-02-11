import requests
from bs4 import BeautifulSoup

# IMDb URL
url = "https://www.imdb.com/search/title/?title_type=feature&release_date=2011-01-01,2011-12-31"

# Headers to mimic a browser visit
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Fetch the page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find movie titles
movie_titles = soup.find_all("h3", class_="ipc-title__text")

# Extract and print the first five movies
for i, title in enumerate(movie_titles[:10], start=1):
    print(f"{i}. {title.text.strip()}")
