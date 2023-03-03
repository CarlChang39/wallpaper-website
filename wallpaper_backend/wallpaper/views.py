from django.views.generic import View
from django.shortcuts import render
import requests

from .scripts import load_config, print_json
from .wallpaper import *

# Create your views here.

config_path = "wallpaper/config.json"

''' Load configs '''
config = load_config(config_path)
API = config["wallpaper"]["API"]
url_prefix = config["wallpaper"]["url_prefix"]

class Wallpaper(View):
    ''' Fetch wallpapers using web crawler '''
    def get(self, request):
        response = request_by_url(API)
        wallpaper_list = get_wallpapers(response["images"], url_prefix)
        context = {
            'wallpaper_list': wallpaper_list
        }
        return render(request, 'index.html', context)