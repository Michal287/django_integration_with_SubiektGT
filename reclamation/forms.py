from django import forms

from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from .models import Reclamation


class DateInput(forms.DateInput):
    input_type = 'date'


class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        exclude = ("status",)
        labels = {
            'client': 'Client',
            'symbol': 'Symbol',
            'product': 'Produkt',
            'producer': 'Producent',
            'option_one': 'Niezgodność towaru z umową (opis wady)',
            'option_two': 'Wadę zauważono',
            'option_three': 'Data wydanania towaru',
            'option_four': 'Numer paragonu',
            'option_five': 'Przyjęto do dypozytu',
            'option_six': 'Żądanie Nabywcy - nidopłata naprawa',
            'option_seven': 'Żądanie Nabywcy - wymiana',
            'option_eight': 'Żądanie Nabywcy - obniżenie ceny(kwota obniżki)',
            'option_nine': 'Żądanie Nabywcy - zwrot pieniędzy',
        }

        widgets = {
            'option_two': DateInput(),
            'option_three': DateInput(),
        }