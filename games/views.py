from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.views import generic
from .models import Game 
from django.core.paginator import Paginator


def home(request):
	return render(request, "games/home.html")
	return HttpResponse("Hello")


class GamesListView(generic.ListView):

    template_name = 'games/games_list.html'
    context_object_name = 'games_list'
    paginate_by = 10

    def get_queryset(self):
        """Return all the objects.""" 
        return Game.objects.all()