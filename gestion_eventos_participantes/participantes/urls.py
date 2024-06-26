from django.urls import path, include
from .views import ParticipanteListView, ParticipanteDetailView, ParticipanteCreateView, ParticipanteUpdateView, ParticipanteDeleteView
from rest_framework.routers import DefaultRouter
from .api import ParticipanteViewSet

router = DefaultRouter()
router.register('', ParticipanteViewSet, 'participantes')

urlpatterns = [
    path('', ParticipanteListView.as_view(), name='participante-list'),
    path('<int:pk>/', ParticipanteDetailView.as_view(), name='participante-detail'),
    path('nuevo/', ParticipanteCreateView.as_view(), name='participante-create'),
    path('<int:pk>/editar/', ParticipanteUpdateView.as_view(), name='participante-update'),
    path('<int:pk>/eliminar/', ParticipanteDeleteView.as_view(), name='participante-delete'),
    path('api/', include(router.urls)),
]
