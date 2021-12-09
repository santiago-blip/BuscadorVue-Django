from rest_framework import serializers
from .models import Buscador


class BuscadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buscador
        fields = '__all__'




class PalabrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buscador
        fields = ('palabra',)
