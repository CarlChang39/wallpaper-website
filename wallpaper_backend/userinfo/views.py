from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class Userinfo(View):
    def get(self, request):
        context = {
            'username': request.session['username']
        }
        return render(request, 'userinfo.html', context)