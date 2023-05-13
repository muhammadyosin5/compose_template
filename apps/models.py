from django.db.models import CharField, IntegerField, Model, ImageField
from django.contrib.auth.models import AbstractUser

# Create your models here. product, user, category

class CustomUser(AbstractUser):
    image = ImageField(upload_to='user_photos', blank=True, null=True)

class Product(Model):
    name = CharField(max_length=255)
    price = IntegerField()

    def __str__(self):
        return self.name


class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name