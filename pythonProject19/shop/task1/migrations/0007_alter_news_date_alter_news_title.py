# Generated by Django 4.2.16 on 2024-12-14 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0006_news_alter_kessel_power'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]