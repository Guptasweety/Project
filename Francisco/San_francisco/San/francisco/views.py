# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView
import requests
from francisco.models import Movie, db

class Sanfrancisco(TemplateView):
    def get(self,request):
        r = requests.get('https://data.sfgov.org/resource/wwmu-gmzc.json', verify=False)
        movie_data = r.json()
        movies_list = {'movies':movie_data}
        return render(request,'movie_list.html',movies_list)    
