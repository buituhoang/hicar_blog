from bs4 import BeautifulSoup
import requests 

def youtubeCrawler(channelUrl):
    channelId = channelUrl.split('/')[-1]
    feefdUrl = "https://www.youtube.com/feeds/videos.xml?channel_id=" + channelId
    file = requests.get(feefdUrl)
    soup = BeautifulSoup(file.text, 'html.parser')
    list = []

    entries = soup.find_all('entry')
    for entry in entries:
        youtubeVideo = {}
        try:
            youtubeVideo['title'] = entry.find('media:title').text
        except:
            youtubeVideo['title'] = ""
        try:
            youtubeVideo['url'] = entry.find('media:content')['url']
        except:
            youtubeVideo['url'] = ""
        try:
            youtubeVideo['thumbnail'] = entry.find('media:thumbnail')['url']
        except:
            youtubeVideo['thumbnail'] = ""
        try:
            youtubeVideo['description'] = entry.find('media:description').text
        except:
            youtubeVideo['description'] = ""
        try:
            youtubeVideo['likes'] = entry.find('media:starrating')['count']
        except:
            youtubeVideo['likes'] = ""
        try:
            youtubeVideo['views'] = entry.find('media:statistics')['views']
        except:
            youtubeVideo['views'] = ""
        list.append(youtubeVideo)
    return list


