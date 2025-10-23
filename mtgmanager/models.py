from django.db import models

class TipoCarta(models.TextChoices):
    CRIATURA = 'Criatura', 'Criatura'
    TERRENO_BASICO = 'Terreno Básico', 'Terreno Básico'
    TERRENO_NAO_BASICO = 'Terreno Não Básico', 'Terreno Não Básico'
    INSTANTANEA = 'Instantânea', 'Instantânea'
    ENCANTAMENTO = 'Encantamento', 'Encantamento'
    FEITICO = 'Feitiço', 'Feitiço'
    PLANESWALKER = 'Planeswalker', 'Planeswalker'
    OUTRO = 'Outro', 'Outro'
    

class Carta(models.Model):
    ESTADOS_CONSERVACAO = [
        ('N', 'Novo'),
        ('U', 'Usado'),
        ('D', 'Danificado'),
    ]

    nome = models.CharField(max_length=100)
    edicao = models.CharField(max_length=100)
    estado_conservacao = models.CharField(max_length=1, choices=ESTADOS_CONSERVACAO)
    quantidade = models.PositiveIntegerField()
    imagem_url = models.URLField(blank=True, null=True)
    tipo = models.CharField(
        max_length=30,
        choices=TipoCarta.choices,
        default=TipoCarta.OUTRO,
    )

    def __str__(self):
        return f"{self.nome} ({self.edicao}) - {self.quantidade}x"


class Deck(models.Model):
    nome = models.CharField(max_length=100)
    formato = models.CharField(max_length=50, default="Commander")
    comandante = models.ForeignKey(
            'Carta',
            on_delete=models.SET_NULL,
            null=True,
            related_name='decks_comandante'
    )

    def __str__(self):
        return self.nome
    
class CartaNoDeck(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='cartas')
    carta = models.ForeignKey('Carta', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def clean(self):
        if self.carta.tipo != TipoCarta.TERRENO_BASICO:
            existentes = CartaNoDeck.objects.filter(deck=self.deck, carta=self.carta)
            if self.pk:
                existentes = existentes.exclude(pk=self.pk)
            if existentes.exists():
                raise ValidationError(f"A carta '{self.carta.nome}' já está no deck e não é um Terreno Básico.")

    def __str__(self):
        return f"{self.carta.nome} no deck {self.deck.nome}"