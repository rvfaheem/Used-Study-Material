from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    type=models.CharField(max_length=20)

class InstitutionType(models.Model):
    Type=models.CharField(max_length=200)


class Category(models.Model):
    INSTITUTIONTYPE=models.ForeignKey(InstitutionType, on_delete=models.CASCADE)
    category_name=models.CharField(max_length=20)

class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=20)
    place=models.CharField(max_length=50)
    District=models.CharField(max_length=50)
    pin=models.BigIntegerField()
    photo=models.CharField(max_length=250)

class Material(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    CATEGORY=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    material_name=models.CharField(max_length=100)
    date=models.DateField(default="2023-10-01")
    image=models.CharField(max_length=250)
    price=models.CharField(max_length=20)
    condition=models.CharField(max_length=100)
    status=models.CharField(max_length=50)

class Request(models.Model):
    MATERIAL=models.ForeignKey(Material,on_delete=models.CASCADE)
    date=models.DateField()
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=20)

class Chat(models.Model):
    FROM_ID=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='fid')
    TO_ID=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='tid')
    date=models.DateField()
    message=models.CharField(max_length=500)

class Complaints(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=500)
    date=models.DateField()
    reply=models.CharField(max_length=500)
    status=models.CharField(max_length=20)

class Feedback(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=500)
    date=models.DateField()

