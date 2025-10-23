from django import forms

class ImportarCartasForm(forms.Form):
    nomes = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}),
        help_text="Cole os nomes das cartas, um por linha."
    )