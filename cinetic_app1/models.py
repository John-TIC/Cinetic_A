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
        return self.Identificacion

class VentaProductos(models.Model):
    IdVenta = models.IntegerField(primary_key=True,unique=True)
    IdEmpleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    FechaVenta = models.DateField(auto_now_add=True, null=False, blank=False)
    def __str__(self):
        return self.IdVenta

class ListaVentaProductos(models.Model):
    IdListaCompra = models.IntegerField(primary_key=True,unique=True)
    IdCombo = models.ForeignKey(Combo, on_delete=models.PROTECT)
    IdProducto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    IdVenta = models.ForeignKey(VentaProductos, on_delete=models.PROTECT)
    Cantidad = models.IntegerField()
    Subtotal = models.IntegerField()

class Pelicula(models.Model):
    IdPelicula = models.IntegerField(primary_key=True,unique=True)
    CodigoPelicula = models.CharField(max_length=10, unique=True)
    NombrePelicula = models.CharField(max_length=30)
    Genero = models.CharField(max_length=20)
    Clasificacion = models.CharField(max_length=12)
    NombreDirector = models.CharField(max_length=40)
    FechaNacimiento = models.DateField(auto_now_add=False, null=False, blank=False)
    Sinopsis = models.CharField(max_length=250)
    Duracion = models.IntegerField()
    def __str__(self):
        return self.CodigoPelicula

class Cinema(models.Model):
    IdCinema = models.IntegerField(primary_key=True,unique=True)
    CodigoCinema = models.CharField(max_length=5)
    Ciudad = models.CharField(max_length=25)
    Telefono = models.CharField(max_length=15)
    Direccion = models.CharField(max_length=40)
    Email = models.CharField(max_length=30)
    def __str__(self):
        return self.CodigoCinema
class Sala(models.Model):
    IdSala = models.IntegerField(primary_key=True,unique=True)
    IdCinema = models.ForeignKey(Cinema, on_delete=models.PROTECT)
    CodigoSala = models.CharField(max_length=5)
    Nombre = models.CharField(max_length=20)
    TipoSala = models.CharField(max_length=5)
    Capacidad = models.IntegerField()
    def __str__(self):
        return self.CodigoSala

class Funcion(models.Model):
    IdFuncion = models.IntegerField(primary_key=True,unique=True)
    IdPelicula = models.ForeignKey(Pelicula, on_delete=models.PROTECT)
    IdSala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    CodigoFuncion = models.CharField(max_length=5)
    Horario = models.CharField(max_length=7)
    Fecha = models.DateField(auto_now_add=False, null=False, blank=False)
    def __str__(self):
        return self.CodigoFuncion

class VentaBoletas(models.Model):
    IdVentaBoletas = models.IntegerField(primary_key=True,unique=True)
    IdEmpleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    FechaVenta = models.DateField(auto_now_add=False, null=False, blank=False)
    def __str__(self):
        return self.IdVentaBoletas
class Boletas(models.Model):
    IdBoleta = models.IntegerField(primary_key=True,unique=True)
    IdFuncion = models.ForeignKey(Funcion, on_delete=models.PROTECT)
    IdVentaBoletas = models.ForeignKey(VentaBoletas, on_delete=models.PROTECT)
    NumeroSilla = models.IntegerField()
    ValorBoleta = models.IntegerField()
