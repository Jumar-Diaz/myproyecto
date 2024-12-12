from rest_framework import serializers
from .models import Recomendacion, Calificacion, CalificacionImage,RecomendacionMovil

class RecomendacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomendacion
        fields = '__all__'
class RecomendacionSerializerMovil(serializers.ModelField):
    class Meta:
        model = RecomendacionMovil
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'

class CalificacionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalificacionImage
        fields = '__all__'