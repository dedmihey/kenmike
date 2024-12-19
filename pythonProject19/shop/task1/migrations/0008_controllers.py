# Generated by Django 4.2.16 on 2024-12-19 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0007_alter_news_date_alter_news_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Controllers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('manufacturer', models.CharField(max_length=30)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
