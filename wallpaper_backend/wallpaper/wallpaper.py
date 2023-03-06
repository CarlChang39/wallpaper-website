import requests
import json

def request_by_url(url):
    ''' Web crawler '''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
    response = requests.get(url, headers).json()
    return response

def get_Bing_wallpapers(image_list, url_prefix):
    ''' Get useful attributes of Bing wallpaper '''
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

def get_Wallhaven_wallpapers(image_list):
    ''' Get useful attributes of Wallhaven wallpaper '''
    wallpaper_list = []
    for image in image_list:
        wallpaper_list.append(
            dict(
                url = image["path"],
            )
        )
    return wallpaper_list