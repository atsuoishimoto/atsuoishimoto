import feedparser
import dateutil.parser

from miyadaiku.site import Site
from miyadaiku.extend import initialized


trans = str.maketrans({
    '[':'&#91;', 
    ']':'&#93;',
    '*':'&#42;',
    '`':'&#96;',
    '\n': ''
})

def get_feed(url):

    feed = feedparser.parse(url)
    return [
        {
            "title": entry["title"].translate(trans),
            "url": entry["link"],
            "published": dateutil.parser.parse(entry["published"])
        }
        for entry in feed["entries"]
    ]

@initialized
def set_feed(site):
    feed1 = get_feed('https://aish.dev/all.atom.xml')
    feed2 = get_feed('https://zenn.dev/atsuoishimoto/feed')
    feeds = reversed(sorted(feed1 + feed2, key=lambda d:(d['published'], d['title'])))

    site.config.add("/", {'feed':feeds[:20]})
    site.rebuild = True
