from django.db import models

# Create your models here.
class Producto(models.Model):
    IdProducto = models.IntegerField(primary_key=True,unique=True)
    CodigoProducto = models.CharField(max_length=10, unique=True)
    NombreProducto = models.CharField(max_length=25)
    ValorCompra = models.IntegerField()
    ValorVenta = models.IntegerField()
    Ciudad = models.CharField(max_length=25)
    Invetario = models.IntegerField()
    def __str__(self):
        return self.CodigoProducto

class Combo(models.Model):
    IdCombo = models.IntegerField(primary_key=True,unique=True)
    CodigoCombo = models.CharField(max_length=10, unique=True)
    NombreCombo = models.CharField(max_length=25)
    Descuento = models.IntegerField()
    def __str__(self):
        return self.CodigoCombo

class IntegraCombo(models.Model):
    IdIntegraCombo = models.IntegerField(primary_key=True,unique=True)
    IdProducto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    IdCombo = models.ForeignKey(Combo, on_delete=models.PROTECT)
    CantidadProducto = models.IntegerField()

class Empleado(models.Model):
    IdEmpleado = models.IntegerField(primary_key=True,unique=True)
    Identificacion = models.CharField(max_length=10, unique=True)
    Nombres = models.CharField(max_length=30)
    Apellidos = models.CharField(max_length=30)
    Direccion = models.CharField(max_length=40)
    Telefono = models.CharField(max_length=15)
    FechaNacimiento = models.DateField(auto_now_add=False, null=False, blank=False)
    Contrasena = models.CharField(max_length=20)
    Ciudad = models.CharField(max_length=25)
    def __str__(self):
        return self.CodigoCombo

class Venta(models.Model):
    IdVenta = models.IntegerField(primary_key=True,unique=True)
    IdEmpleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    FechaVenta = models.DateField(auto_now_add=True, null=False, blank=False)

class ListaCompra(models.Model):
    IdListaCompra = models.IntegerField(primary_key=True,unique=True)
    IdCombo = models.ForeignKey(Combo, on_delete=models.PROTECT)
    IdProducto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    IdVenta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    Cantidad = models.IntegerField()
    Subtotal = models.IntegerField()

