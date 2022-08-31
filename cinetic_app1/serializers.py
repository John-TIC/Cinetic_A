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

class Venta_Serializer(serializers.ModelSerializer):
    empleado = Empleado_Serializer(read_only=True)
    empleado_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Empleado.objects.all(), source='empleado')
    class Meta:
        model = Venta
        fields = '__all__'

class ListaCompra_Serializer(serializers.ModelSerializer):
    producto = Producto_Serializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Producto.objects.all(), source='producto')
    combo = Combo_Serializer(read_only=True)
    combo_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Combo.objects.all(), source='combo')
    venta = Venta_Serializer(read_only=True)
    venta_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Venta.objects.all(), source='venta')
    class Meta:
        model = ListaCompra
        fields = '__all__'