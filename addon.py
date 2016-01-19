from xbmcswift2 import Plugin, xbmcgui
from resources.lib import skepticsscraper

plugin = Plugin()

PODCAST_URL = 'http://www.theskepticsguide.org/podcast/sgu'

@plugin.route('/')
def main_menu():
    
    items = [
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('latest_podcast'),
        }
    ]

    return items


@plugin.route('/latest/')
def latest_podcast():

    content = skepticsscraper.get_podcast(PODCAST_URL)
    
    items = []
    for i in content:
        items.append({
            'label': i['label'],
            'path': plugin.url_for('play_podcasts', url=i['path']),
            'thumbnail': i['thumbnail'],
        })

    return items


@plugin.route('/latest/<url>')
def play_podcast(url)
    


if __name__ == '__main__':
    plugin.run()
