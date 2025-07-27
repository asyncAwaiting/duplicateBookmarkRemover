from bs4 import BeautifulSoup

# Load and parse your bookmarks file.
# This must be an HTML file! (HTML is the standard format when you export
# from a web browser).
with open('~/Downloads/bookmarks_7_27_25.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')
