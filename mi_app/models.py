from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Presupuesto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    numero = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f"Presupuesto #{self.numero} para {self.cliente.nombre}"

class Revestimiento(models.Model):
    ancho = models.DecimalField(max_digits=5, decimal_places=2)
    alto = models.DecimalField(max_digits=5, decimal_places=2)
    tipo = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    class Meta:
        abstract = True

class Vidrio(Revestimiento):
    espesor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Vidrio {self.tipo} ({self.ancho}x{self.alto}, {self.espesor} mm)"

class Panel(Revestimiento):
    material = models.CharField(max_length=100)

    def __str__(self):
        return f"Panel {self.tipo} ({self.ancho}x{self.alto}, {self.material})"

class Lama(Revestimiento):
    def __str__(self):
        return f"Lama {self.tipo} ({self.ancho}x{self.alto}, {self.color})"

class PVC(models.Model):
    item = models.CharField(max_length=100)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.item} - ${self.precio_unitario}"

class Item(models.Model):
    class Meta:
        abstract = True

    ancho = models.DecimalField(max_digits=5, decimal_places=2)
    alto = models.DecimalField(max_digits=5, decimal_places=2)
    tipo = models.CharField(max_length=100)

class Ventana(Item):
    revestimiento_vidrio = models.ForeignKey(Vidrio, on_delete=models.CASCADE, null=True, blank=True)
    revestimiento_panel = models.ForeignKey(Panel, on_delete=models.CASCADE, null=True, blank=True)
    revestimiento_lama = models.ForeignKey(Lama, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Ventana {self.tipo} ({self.ancho}x{self.alto})"

class Puerta(Item):
    revestimiento_vidrio = models.ForeignKey(Vidrio, on_delete=models.CASCADE, null=True, blank=True)
    revestimiento_panel = models.ForeignKey(Panel, on_delete=models.CASCADE, null=True, blank=True)
    revestimiento_lama = models.ForeignKey(Lama, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Puerta {self.tipo} ({self.ancho}x{self.alto})"

class DetallePresupuesto(models.Model):
    presupuesto = models.ForeignKey(Presupuesto, related_name='detalles', on_delete=models.CASCADE)
    ventana = models.ForeignKey(Ventana, on_delete=models.CASCADE, null=True, blank=True)
    puerta = models.ForeignKey(Puerta, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"Detalle #{self.id} del Presupuesto #{self.presupuesto.numero}"

