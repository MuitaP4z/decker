from django.db import transaction
from django.shortcuts import get_object_or_404
from .models import Carta, Deck, CartaNoDeck

# Exemplo de Transação
@transaction.atomic
def aficionar_carta_ao_deck(deck_id, carta_id, quantidade):
    deck = get_object_or_404(Deck, id=deck_id)
    carta = get_object_or_404(carta, id=carta_id)

    if carta.quantidade < quantidade:
        raise ValueError("Quantidade insuficiente da carta na coleção.")

        CartaNoDeck.objects.create(deck=deck, carta=carta, quantidade=quantidade)

        carta.quantidade -= quantidade
        carta.save()