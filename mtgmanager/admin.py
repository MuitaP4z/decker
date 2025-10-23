from django.urls import path
from django.shortcuts import render, redirect
from django.contrib import admin, messages
from django.contrib import admin
from django.utils.html import format_html
from django.contrib import messages
from .models import Carta
from .models import Deck
from .models import CartaNoDeck
from .models import TipoCarta
from .forms import ImportarCartasForm
from .utils import buscar_carta_scryfall



@admin.register(Carta)
class CartaAdmin(admin.ModelAdmin):
    change_list_template = "admin/importar_cartas_changelist.html"
    list_display = ('nome', 'edicao', 'estado_conservacao', 'quantidade', 'imagem_preview')
    search_fields = ('nome', 'edicao')
    list_filter = ('estado_conservacao', 'edicao')
    actions = ['importar_dados_scryfall']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('importar-cartas/', self.admin_site.admin_view(self.importar_cartas_view), name='importar-cartas'),
        ]
        return custom_urls + urls


    def imagem_preview(self, obj):
        if obj.imagem_url:
            return format_html('<img src="{}" width="50" height="70" />', obj.imagem_url)
        return "-"
    imagem_preview.short_description = 'Imagem'

    @admin.action(description="Importar dados da Scryfall")
    def importar_dados_scryfall(self, request, queryset):
        for carta in queryset:
            dados = buscar_carta_scryfall(carta.nome)
            if dados:
                carta.edicao = dados['edicao']
                carta.imagem_url = dados['imagem_url']
                carta.save()
                self.message_user(request, f"Dados de '{carta.nome}' importados com sucesso!", messages.SUCESS)
            else:
                self.message_user(request, f"Não foi possível encontrar '{carta.nome}' na Scryfall.", messages.WARNING)

    def importar_cartas_view(self, request):
        if request.method == 'POST':
            form = ImportarCartasForm(request.POST)
            if form.is_valid():
                nomes = form.cleaned_data['nomes'].splitlines()
                sucesso = erros = 0

                for nome in nomes:
                    dados = buscar_carta_scryfall(nome.strip())
                    if dados:
                        carta, criada = Carta.objects.get_or_create(
                            nome=nome.strip(),
                            defaults={
                                'edicao': dados['edicao'],
                                'imagem_url': dados['imagem_url'],
                                'quantidade': 1,
                                'estado_conservacao': 'Novo',
                                'tipo': TipoCarta.OUTRO,
                            }
                        )
                        if not criada:
                            carta.edicao = dados['edicao']
                            carta.imagem_url = dados['imagem_url']
                            carta.save()
                        sucesso += 1
                    else:
                        erros += 1

                messages.success(request, f"{sucesso} cartas importadas com sucesso.")
                if erros:
                    messages.warning(request, f"{erros} cartas não foram encontradas.")
                return redirect("..")
        else:
            form = ImportarCartasForm()

        return render(request, "admin/importar_cartas.html", {"form": form})

@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ('nome', 'formato')  # ajuste conforme os campos que você definiu
    search_fields = ('nome',)

@admin.register(CartaNoDeck)
class CartaNoDeckAdmin(admin.ModelAdmin):
    list_display = ('deck', 'carta', 'quantidade')
