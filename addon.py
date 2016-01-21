from xbmcswift2 import Plugin, xbmcgui
from resources.lib import skepticsscraper
import pyxbmct.addonwindow as pyxbmct
import os

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

@plugin.route('/latest_podcast/')
def latest_podcast():

    content = skepticsscraper.get_latest_podcast(PODCAST_URL)
    
    items = []
    for i in content:
        items.append({
            'label': i['label'],
            'path': plugin.url_for('play_podcast', url=i['path']),
            'thumbnail': i['thumbnail'],
        })

    return items

@plugin.route('/latest_podcast/<url>')
def play_podcast(url):
    WINDOW_NAME = 'Skeptics Guide to the Universe'
    WORD = """What's the Word: """
    NEWS_ITEMS_NAME = "News Items"

    item = skepticsscraper.get_podcast_content(url)

    for i in item:
        sub_title = i['title']
        what_is_word = i['word']
             
    window = PodcastWindow(WINDOW_NAME)
    window.set_sub_title(sub_title)
    window.set_podcast_content(WORD + what_is_word)
    window.doModal()
    del window

class PodcastWindow(pyxbmct.AddonDialogWindow):
    
    def __init__(self, title=''):
        super(PodcastWindow, self).__init__(title)
        self.setGeometry(900,650, 3, 3)
        # connect a key action (Backspace) to close window
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)

    def set_sub_title(self, sub_title):
        self.textbox = pyxbmct.TextBox()
        self.placeControl(self.textbox, 0, 0, 2, 4)
        self.textbox.setText(sub_title)

    def set_podcast_content(self, what_is_word):
        self.label = pyxbmct.Label(what_is_word)
        self.placeControl(self.label, 0.3, 0)
        
    def set_news_items(self, NEWS_ITEMS_NAME
 

if __name__ == '__main__':
    plugin.run()
