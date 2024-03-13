from django.db import models
from django.core.validators import RegexValidator



# Create your models here.
class Persona(models.Model):
    
    #Campos que tendra la tabla persona
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100, verbose_name="Nombre")
    last_name = models.CharField(max_length = 100, verbose_name="Apellido")
    email = models.EmailField(max_length = 200, unique = True) 
    phone = models.CharField(max_length = 10)
    cedula = models.CharField(max_length = 10, 
                              unique = True,
                              validators=[RegexValidator(
                                  regex=r'^\d+$', 
                                  message='No se permite ingresar letras, solo números')])
                                    #Validar la cedula solo 10 digitos y numeros
    
    
    class Meta:
        verbose_name = "CRUD Usuario"
        verbose_name_plural = "CRUD Usuarios"
        ordering = ["-id"]
        
    def __str__(self):
        return str(self.id) + " " + self.name + " " + self.last_name
        #Mostrar en administracion django