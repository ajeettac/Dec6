from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name
class Course(models.Model):
    name=models.CharField(max_length=25)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='course')
    
    def __str__(self):
        return self.name