from django import forms
from .models import Evento
from participantes.models import Participante
from django import forms
from .models import Evento, Asistencia

class EventoForm(forms.ModelForm):
    participantes = forms.ModelMultipleChoiceField(queryset=Participante.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion', 'fecha', 'hora', 'ubicacion', 'participantes']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'participantes': forms.CheckboxSelectMultiple,
        }
        labels = {
            'nombre': 'Nombre del evento',
            'descripcion': 'Descripción',
            'fecha': 'Fecha',
            'hora': 'Hora',
            'ubicacion': 'Ubicación',
        }

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['evento', 'participante']
