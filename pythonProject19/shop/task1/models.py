from django.db import models

# Create your models here.
class Buyer(models.Model):
    name=models.CharField(max_length=20)
    balance=models.DecimalField(decimal_places=2, max_digits=8, default='default balance')
    age=models.IntegerField(default='default age')


class Game(models.Model):
    title=models.CharField(max_length=20)
    cost=models.DecimalField(decimal_places=2, max_digits=8, default='default cost')
    size=models.IntegerField(default='default size')
    description=models.TextField(default='default description')
    age_limited=models.BooleanField(default=False)
    buyer=models.ManyToManyField(Buyer, related_name='games')