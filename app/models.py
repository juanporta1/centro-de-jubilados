from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Member(models.Model):
    name = models.CharField("Nombre",max_length=100)
    lastname = models.CharField("Apellido",max_length=100)
    dni = models.CharField("DNI",max_length=20, unique=True)
    memberNumber = models.CharField("Número de Socio",max_length=20, unique=True)
    phone = models.CharField("Teléfono",max_length=20, blank=True, null=True)
    SEXS = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    sex = models.CharField("Sexo",max_length=1, choices=SEXS)
    birthdate = models.DateField("Fecha de Nacimiento", blank=True, null=True)
    home = models.CharField("Domicilo",max_length=200, blank=True, null=True)
    memberRegistrationDate = models.DateField("Fecha de Admision", default=timezone.now)
    email = models.EmailField("Email", max_length=254, blank=True, null=True)
    observations = models.TextField("Observaciones", blank=True, null=True)
    
    ACTIVITY = [
        (1, 'Sí'),
        (0, 'No'),
    ]
    isActive = models.IntegerField("Activo", default=1, choices=ACTIVITY, max_length=1)
    
    def __str__(self):
        return f"{self.name} {self.lastname} - Num. de Socio: {self.memberNumber} - DNI: {self.dni}"
    class Meta:
        verbose_name = "Socio"        # singular
        verbose_name_plural = "Socios" # plural

class Settings(models.Model):
    paymentAmount = models.DecimalField("Monto de la Cuota", max_digits=10, decimal_places=2, default=0.00)
    class Meta:
        verbose_name = "Configuraciones"        # singular
        verbose_name_plural = "Configuración" # plural
    def __str__(self):
        return f"Configuración - Monto de la Cuota: {self.paymentAmount}"
    

      
class Payment(models.Model):
    member = models.ForeignKey(Member, verbose_name="Socio", on_delete=models.CASCADE)
    formNumber = models.CharField("Número de Planilla", max_length=50, blank=True, null=True)
    amount = models.DecimalField("Monto",decimal_places=2, max_digits=10, default=0.0)
    MONTHS = [
    (1, 'Enero'),
    (2, 'Febrero'),
    (3, 'Marzo'),
    (4, 'Abril'),
    (5, 'Mayo'),
    (6, 'Junio'),
    (7, 'Julio'),
    (8, 'Agosto'),
    (9, 'Septiembre'),
    (10, 'Octubre'),
    (11, 'Noviembre'),
    (12, 'Diciembre'),
    ]
    month = models.IntegerField("Mes de la Cuota", choices=MONTHS, default=datetime.datetime.now().month)
    date = models.DateField("Fecha de Pago", blank=True, null=True)
    
    PAYMENT_METHODS = [
        ('Efectivo', 'Efectivo'),
        ('Transferencia', 'Transferencia'),
        ('Otro', 'Otro'),
    ]
    method = models.CharField("Método de Pago", max_length=50, choices=PAYMENT_METHODS)
    observations = models.TextField("Observaciones", blank=True, null=True)
    
    def __str__(self):
        return f"Socio: {self.member.name} {self.member.lastname} - Num. de Socio: {self.member.memberNumber} - Mes: {self.get_month_display()} - Monto: {self.amount} - Fecha de Pago: {self.date}"
    
    class Meta:
        verbose_name = "Pago"        # singular
        verbose_name_plural = "Pagos" # plural
        
      
class MemberActivityLog(models.Model):
    member = models.ForeignKey(Member, verbose_name="Socio", on_delete=models.CASCADE)
    date = models.DateTimeField("Fecha",auto_now_add=True)
    ACTIVE = [
        (1, 'Activo'),
        (0, 'Inactivo'),
    ]
    activity = models.IntegerField("Paso a",choices=ACTIVE, max_length=1)
    class Meta:
        verbose_name = "Registro de Actividad del Socio"        # singular
        verbose_name_plural = "Registros de Actividad de los Socios"