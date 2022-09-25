from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __str__(self):
        return  self.name

class Team(models.Model):
    t_name=models.CharField(max_length=100)
    t_img=models.ImageField(upload_to='t_pics')
    t_desc=models.TextField()
    def __str__(self):
        return self.t_name