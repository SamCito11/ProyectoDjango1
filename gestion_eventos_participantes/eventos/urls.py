from django.urls import path, include
from .views import EventoListView, EventoDetailView, EventoCreateView, EventoUpdateView, EventoDeleteView
from rest_framework.routers import DefaultRouter
from .api import EventoViewSet

router = DefaultRouter()
router.register('', EventoViewSet, 'eventos')

urlpatterns = [
    path('', EventoListView.as_view(), name='evento-list'),
    path('<int:pk>/', EventoDetailView.as_view(), name='evento-detail'),
    path('nuevo/', EventoCreateView.as_view(), name='evento-create'),
    path('<int:pk>/editar/', EventoUpdateView.as_view(), name='evento-update'),
    path('<int:pk>/eliminar/', EventoDeleteView.as_view(), name='evento-delete'),
    path('api/', include(router.urls)),
]
