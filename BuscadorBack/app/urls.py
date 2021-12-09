from django.urls import path,include
from rest_framework import routers
from .views import homeBuscador,RetornarPalabras

router = routers.DefaultRouter()
router = routers.DefaultRouter()
router.register('reportes',homeBuscador,basename="reportes")
router.register('listado',RetornarPalabras,basename="listado")

app_name="app"
urlpatterns=[
    path('',include(router.urls))
]
