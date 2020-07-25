import feedparser
import dateutil.parser
import pprint
def get_feed(url):
    entries = feedparser.parse(url)["entries"]
    return [
        {
            "title": entry["title"],
            "url": entry["link"],
            "published": dateutil.parser.parse(entry["published"])
        }
        for entry in entries
    ]


pprint.pprint(get_feed('https://aish.dev/all.atom.xml'))
