from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Participante

class ParticipanteListView(ListView):
    model = Participante
    template_name = 'participantes/participante_list.html'

class ParticipanteDetailView(DetailView):
    model = Participante
    template_name = 'participantes/participante_detail.html'

class ParticipanteCreateView(CreateView):
    model = Participante
    template_name = 'participantes/participante_form.html'
    fields = ['nombre', 'apellido', 'documento', 'email', 'estado']
    success_url = reverse_lazy('participante-list')

class ParticipanteUpdateView(UpdateView):
    model = Participante
    template_name = 'participantes/participante_form.html'
    fields = ['nombre', 'apellido', 'documento', 'email', 'estado']
    success_url = reverse_lazy('participante-list')

class ParticipanteDeleteView(DeleteView):
    model = Participante
    template_name = 'participantes/participante_confirm_delete.html'
    success_url = reverse_lazy('participante-list')
