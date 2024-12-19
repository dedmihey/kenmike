# Generated by Django 4.2.16 on 2024-12-19 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0008_controllers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Burners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('power', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
