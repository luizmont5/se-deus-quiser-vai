from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    nascimento = models.DateField()
    cpf =models.IntegerField()
    email = models.EmailField()
    endereco = models.TextField(max_length=255)
    doenca = models.TextField(max_length=255)
    password = models.TextField(max_length=255)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    class Appointment(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    
    def cancel(self):
        self.user = None
        self.save()

def save(self, *args, **kwargs):
        if Usuario.objects.filter(nome=self.nome, nascimento=self.nascimento, cpf=self.cpf,email=self.email,endereco=self.endereco,doenca=self.doenca,password=self.password).exists():
            pass
        else:
            super(Usuario, self).save(*args, **kwargs)
            