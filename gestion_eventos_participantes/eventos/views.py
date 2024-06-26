from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Evento, Asistencia
from participantes.models import Participante
from .forms import EventoForm

class EventoListView(ListView):
    model = Evento
    template_name = 'eventos/evento_list.html'

class EventoDetailView(DetailView):
    model = Evento
    template_name = 'eventos/evento_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['participantes'] = self.object.participantes.all()
        return context

class EventoCreateView(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/evento_form.html'
    success_url = reverse_lazy('evento-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        participantes = self.request.POST.getlist('participantes')
        for participante_id in participantes:
            Asistencia.objects.create(evento=self.object, participante_id=participante_id)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['participantes'] = Participante.objects.all()
        return context

class EventoUpdateView(UpdateView):
    model = Evento
    template_name = 'eventos/evento_form.html'
    fields = ['nombre', 'descripcion', 'fecha', 'hora', 'ubicacion']
    success_url = reverse_lazy('evento-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['participantes'] = Participante.objects.all()
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        Asistencia.objects.filter(evento=self.object).delete()
        participantes = self.request.POST.getlist('participantes')
        for participante_id in participantes:
            Asistencia.objects.create(evento=self.object, participante_id=participante_id)
        return response

class EventoDeleteView(DeleteView):
    model = Evento
    template_name = 'eventos/evento_confirm_delete.html'
    success_url = reverse_lazy('evento-list')
