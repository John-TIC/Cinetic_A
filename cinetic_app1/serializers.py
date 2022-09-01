from rest_framework import serializers
from cinetic_app1.models import *


class Producto_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class Combo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = '__all__'

class IntegraCombo_Serializer(serializers.ModelSerializer):
    producto = Producto_Serializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Producto.objects.all(), source='producto')
    combo = Combo_Serializer(read_only=True)
    combo_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Combo.objects.all(), source='combo')
    class Meta:
        model = IntegraCombo
        fields = '__all__'

class Empleado_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class VentaProductos_Serializer(serializers.ModelSerializer):
    empleado = Empleado_Serializer(read_only=True)
    empleado_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Empleado.objects.all(), source='empleado')
    class Meta:
        model = VentaProductos
        fields = '__all__'

class ListaVentaProductos_Serializer(serializers.ModelSerializer):
    producto = Producto_Serializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Producto.objects.all(), source='producto')
    combo = Combo_Serializer(read_only=True)
    combo_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Combo.objects.all(), source='combo')
    venta = VentaProductos_Serializer(read_only=True)
    venta_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=VentaProductos.objects.all(), source='venta')
    class Meta:
        model = ListaVentaProductos
        fields = '__all__'

class Pelicula_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'

class Cinema_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'

class Sala_Serializer(serializers.ModelSerializer):
    cinema = Cinema_Serializer(read_only=True)
    cinema_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Cinema.objects.all(), source='cinema')
    class Meta:
        model = ListaVentaProductos
        fields = '__all__'

class Funcion_Serializer(serializers.ModelSerializer):
    pelicula = Pelicula_Serializer(read_only=True)
    pelicula_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Pelicula.objects.all(), source='pelicula')
    sala = Sala_Serializer(read_only=True)
    sala_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Sala.objects.all(), source='sala')
    class Meta:
        model = Funcion
        fields = '__all__'

class VentaBoletas_Serializer(serializers.ModelSerializer):
    empleado = Empleado_Serializer(read_only=True)
    empleado_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Empleado.objects.all(), source='emplado')
    class Meta:
        model = VentaBoletas
        fields = '__all__'

class Boletas_Serializer(serializers.ModelSerializer):
    funcion = Funcion_Serializer(read_only=True)
    funcion_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Funcion.objects.all(), source='funcion')
    ventaboletas = VentaBoletas_Serializer(read_only=True)
    ventaboletas_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=VentaBoletas.objects.all(), source='ventaboletas')
    class Meta:
        model = Boletas
        fields = '__all__'