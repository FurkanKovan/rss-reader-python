import Channel.constants as const
import requests
from bs4 import BeautifulSoup


class Channel:
    def __init__(self, name):
        self.name = name
        super(Channel, self).__init__()

    def getUrl(self):
        url = f"{const.BASE_URL}@{self.name}"
        return url

    def getChannelId(self, url):
        try:
            website = requests.get(url)
            soup = BeautifulSoup(website.content, "html.parser")
            channel_id = soup.find("meta", attrs={"itemprop": "channelId"}).get(
                "content"
            )
        except AttributeError:
            print(
                "\nAn error has occured. Please make sure the Youtube channel exists.\n"
            )
            raise SystemExit()
        except requests.exceptions.RequestException as err:
            print(
                "\nAn error has occured. Please make sure the Youtube channel exists.\n"
            )
            raise SystemExit(err)
        return channel_id

    def getMainPageVideos(self, url, channel_id):
        url = requests.get(f"{const.FEEDS_URL}?channel_id={channel_id}")
        soup = BeautifulSoup(url.content, "xml")
        entries = soup.find_all("entry")

        for entry in entries:
            title = entry.title.text
            pDate = entry.published.text.split(sep="T")[0]
            link = entry.link["href"]
            print(
                f"\nTitle: {title}\n\nPublished on: {pDate}\nVideo Link: {link}\n\n---------------------"
            )
