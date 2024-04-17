from django.db import models

# Create your models here.
class teacherr(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    department=models.TextField()
    age=models.IntegerField()
    place=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()
    photo=models.FileField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

class teacherr(models.Model):
        firstname = models.CharField(max_length=100)
        lastname = models.CharField(max_length=100)
        gender=models.TextField()
        age = models.IntegerField()
        place = models.CharField(max_length=100)
        phone = models.IntegerField()
        email = models.EmailField()
        photo = models.FileField()
        username = models.CharField(max_length=100)
        password = models.CharField(max_length=100)

        def __str__(self):
            return self.firstname