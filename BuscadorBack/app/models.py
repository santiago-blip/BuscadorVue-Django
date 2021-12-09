from django.db import models

# Create your models here.
class Buscador(models.Model):
    palabra = models.CharField(max_length=100)
    busquedas_totales = models.IntegerField()
    primer_busqueda = models.DateField(auto_now_add=True,null=True,blank=True)
    ultima_busqueda = models.DateField(auto_now=True,null=True,blank=True)
    ultimos_resultados = models.IntegerField(null=True,blank=True)