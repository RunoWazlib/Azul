from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import TileBag

# Create your views here.
# Start a new game
def start_new_game(request):
    set_start_tiles = TileBag.objects()[:5]
    template = loader.get_template("new_game/start_new_game")
    context = {"set_start_tiles":set_start_tiles}
    return HttpResponse(template.render(context, request))