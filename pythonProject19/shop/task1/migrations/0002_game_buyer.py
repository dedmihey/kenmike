# Generated by Django 4.2.16 on 2024-12-03 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='buyer',
            field=models.ManyToManyField(related_name='games', to='task1.buyer'),
        ),
    ]
