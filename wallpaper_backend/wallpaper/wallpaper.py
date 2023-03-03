import requests
import json

def request_by_url(url):
    ''' Web crawler '''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
    response = requests.get(url, headers).json()
    return response

def get_wallpapers(image_list, url_prefix):
    ''' Get useful attributes from web crawler response '''
    wallpaper_list = []
    for image in image_list:
        wallpaper_list.append(
            dict(
                title = image["title"],
                url = url_prefix + image["url"],
                copyright = image["copyright"],
                copyrightlink = image["copyrightlink"]
            )
        )
    return wallpaper_list