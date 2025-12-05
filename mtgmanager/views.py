from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Deck, CartaNoDeck
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import UserRegisterForm

class DeckDetailView(DetailView):
    model = Deck
    template_name = "mtgmanager/deck_detail.html"
    context_object_name = 'deck'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartas_no_deck'] = CartaNoDeck.objects.filter(deck=self.object).select_related('carta')
        return context

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/')  # ou 'login'
    else:
        form = UserRegisterForm()

    return render(request, "register.html", {"form": form})

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

