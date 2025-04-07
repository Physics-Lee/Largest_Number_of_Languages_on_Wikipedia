import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# URL of the Wikipedia page with the table
url = 'https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_articles_written_in_the_greatest_number_of_languages'

# Send a GET request to fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the first table on the page (or modify this if there are multiple tables)
table = soup.find('table')

# Use pandas to parse the HTML table
df = pd.read_html(str(table))[0]

# Save the table as a CSV file
csv_file_path = os.path.join(os.getcwd(), 'wikipedia_table.csv')
df.to_csv(csv_file_path, index=False)

print("Table saved as 'wikipedia_table.csv'")