from django.urls import path, include
from . import views
from django.conf.urls import url
from rest_framework import routers




# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()


urlpatterns = [
    path('', views.ModuloList.as_view(), name='index'),
    url('api/modulos/', views.ModuloViewSet.as_view(), name="modulos-api"),
    #url(r'^inicio/$', views.ModuloList.as_view(), name="modulos-detail"),
    url('nivel/(?P<nivel>[0-9]+)/exercicio/(?P<id>[0-9]+)/$', views.ExercicioAprendizagemList.as_view(),name='exercicio-detail'),
    url('api/nivel/(?P<id>[0-9]+)/$', views.NivelViewSet.as_view(),name='niveis-api'),
    url('api/exercicio/(?P<id>[0-9]+)/$', views.ExercicioViewSet.as_view(),name='exercicios-api'),
    url('api/recompensa/(?P<id>[0-9]+)/$', views.RecompensaViewSet.as_view(),name='recompensas-api'),
    url(r'^', include(router.urls)),

    #path('nivel/', NivelViewSet.as_view(), name="niveis-all")
]