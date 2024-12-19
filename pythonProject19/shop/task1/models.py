from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default='default balance')
    age = models.IntegerField(default='default age')

    def __str__(self):
        return self.name

    objects = models.Manager()


class Game(models.Model):
    title = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=8, decimal_places=2, default='default cost')
    size = models.IntegerField(default='default size')
    description = models.TextField(default='default description')
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')


class Kessel(models.Model):
    title = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default='default cost')
    power = models.IntegerField(default='default power')
    description = models.TextField(default='default description')
    # age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='kesseln')
    objects = models.Manager()

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(default='default content')
    date = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Controllers(models.Model):
    name = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Burners(models.Model):
    title = models.CharField(max_length=30)
    power = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    objects = models.Manager()

    def __str__(self):
        return self.title


class Children(models.Model):
    name = models.CharField(max_length=10)
    edge = models.IntegerField()
    occupation = models.CharField(max_length=10)
    objects = models.Manager()

    def __str__(self):
        return self.name
