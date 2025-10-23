from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Deck, CartaNoDeck
from django.http import HttpResponse

class DeckDetailView(DetailView):
    model = Deck
    template_name = "mtgmanager/deck_detail.html"
    context_object_name = 'deck'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartas_no_deck'] = CartaNoDeck.objects.filter(deck=self.object).select_related('carta')
        return context


def home(request):
    return HttpResponse("<h1>Bem-vindo ao decker.io</h1><p>Use o menu para acessar o painel administrativo.</p>")
