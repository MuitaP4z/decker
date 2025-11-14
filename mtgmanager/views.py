from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Deck, CartaNoDeck
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

class DeckDetailView(DetailView):
    model = Deck
    template_name = "mtgmanager/deck_detail.html"
    context_object_name = 'deck'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartas_no_deck'] = CartaNoDeck.objects.filter(deck=self.object).select_related('carta')
        return context


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return redirect('dashboard')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
