from django.db import models

# Create your models here.
class Volunteer(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=30)
    message=models.TextField()

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.name

class Cause(models.Model):
    name=models.CharField(max_length=30)
    img=models.ImageField()
    detail=models.CharField(max_length=500)
    raised=models.FloatField()
    goal=models.FloatField()

    def __str__(self):
        return self.name

class Donate(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    amount=models.FloatField()

    def __str__(self):
        return self.name
    
