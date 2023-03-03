from bs4 import BeautifulSoup
import requests

try:
    url = requests.get('https://www.youtube.com/feeds/videos.xml?channel_id=UCrG27KDq7eW4YoEOYsalU9g')
    # The channel : https://www.youtube.com/@NevsinMenguofficial
except requests.exceptions.RequestException as err:
    print("\nAn error has occured. Please nake sure the link is valid.\n")
    raise SystemExit(err)

soup = BeautifulSoup(url.content, 'xml')
entries = soup.find_all('entry')

for entry in entries:
    title = entry.title.text
    pDate = entry.published.text.split(sep='T')[0]
    link = entry.link['href']
    print(f"\nTitle: {title}\n\nPublished on: {pDate}\nVideo Link: {link}\n\n---------------------")
