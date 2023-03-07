from django.views.generic import View
from django.shortcuts import render
import requests

from .scripts import load_config, print_json
from .wallpaper import *

# Create your views here.

config_path = "wallpaper/config.json"

''' Load configs '''
config = load_config(config_path)
Bing_API = config["wallpaper"]["Bing_API"]
Bing_url_prefix = config["wallpaper"]["Bing_url_prefix"]
Wallhaven_API = config["wallpaper"]["Wallhaven_API"]

class Wallpaper(View):
    ''' Fetch wallpapers using web crawler '''
    def get(self, request):
        if(request.path.find('bing') != -1):
            ''' Get Bing wallpapers '''
            response = request_by_url(Bing_API)
            wallpaper_list = get_Bing_wallpapers(response["images"], Bing_url_prefix)
            context = {
                'wallpaper_list': wallpaper_list
            }
            return render(request, 'bing.html', context)
            
        elif(request.path.find('latest') != -1 or request.path.find('hot') != -1 
                or request.path.find('toplist') != -1 or request.path.find('random') != -1):
            ''' Get Wallhaven wallpapers '''
            sorting = request.path.replace('/', '').replace('wallpaper', '')
            page = request.GET.get('page')
            if(page == None):
                page = "1"
            response = request_by_url(Wallhaven_API+'?sorting='+sorting+'&page='+page)
            wallpaper_list = get_Wallhaven_wallpapers(response["data"])
            context = {
                'path': request.path,
                'sorting': sorting,
                'wallpaper_list': wallpaper_list
            }
            return render(request, 'wallhaven.html', context)
        
        else:
            ''' Search Wallhaven wallpapers '''
            pass
        