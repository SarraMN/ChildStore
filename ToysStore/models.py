from django.db import models
from django.db.models.fields.related import ManyToManyField, OneToOneField

dir='Storage/Images'

class Parent(models.Model):
  firtName=models.CharField(name='firt_name', max_length=50)
  lastName=models.CharField(name='last_name', max_length=50)                                                         
  Birthday=models.DateField() 
  photo=models.ImageField(upload_to=dir) 
  
class Child(models.Model):
  firtName=models.CharField(name='firt_name', max_length=50)
  lastName=models.CharField(name='last_name', max_length=50)                                                         
  anneEtude=models.PositiveIntegerField()
  photo=models.ImageField(upload_to=dir) 
  idParent=models.ForeignKey(Parent, on_delete=models.CASCADE)

class place(models.Model):
  longitude=models.FloatField()
  attitude=models.FloatField(blank=True)
  ChildPlaces=ManyToManyField(Child) 
  
class emplacement(models.Model):
  name=models.CharField
  adresse=models.CharField(max_length=100)
  remarque=models.CharField(max_length=50) 
  empChild=ManyToManyField(Child)

class rapport(models.Model):
  date=models.DateField() 
  text=models.CharField(max_length=50)
  problems=models.CharField(max_length=50)  
  benefice=models.CharField(max_length=100)

class task(models.Model):
  name=models.CharField(max_length=50)
  dateDebut=models.DateField() 
  dateFin=models.DateField() 
  type=models.CharField(max_length=50)
  state=models.CharField(max_length=50)
  idChild=models.ForeignKey(Child, on_delete=models.CASCADE)
  idEmplacement=models.ForeignKey(emplacement, on_delete=models.CASCADE)
  idRapport=OneToOneField(rapport, on_delete=models.CASCADE)

class message(models.Model):
  contenu=models.CharField(max_length=50)
  date=models.DateField(name="date_message") 
  idChild=models.ForeignKey(Child, on_delete=models.CASCADE)
                                     
# Create your models here.
