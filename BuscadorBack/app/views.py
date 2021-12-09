from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Buscador
from .serializers import BuscadorSerializer, PalabrasSerializer

# Create your views here.


class homeBuscador(viewsets.ModelViewSet):
    serializer_class = BuscadorSerializer
    queryset = Buscador.objects.all()
       

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            #name = serializer.validated_data.get("palabra")
            serializar_lista = BuscadorSerializer(Buscador.objects.all(), many=True)
            for item in serializar_lista.data:
                if item['palabra'].lower() == serializer.validated_data.get("palabra").lower():
                    param = Buscador.objects.get(palabra=serializer.validated_data.get("palabra"))
                    param.busquedas_totales = param.busquedas_totales + 1
                    param.ultimos_resultados = serializer.validated_data.get("ultimos_resultados")
                    param.save()
                    return Response({'lista': serializar_lista.data})
                    break
            serializer.save()
            return Response({'lista': serializar_lista.data})
        else:
            return Response(serializer.errors)




class RetornarPalabras(viewsets.ModelViewSet):
    queryset = Buscador.objects.all()
    serializer_class = PalabrasSerializer
