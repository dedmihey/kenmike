# Generated by Django 4.2.16 on 2024-12-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0005_kessel'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField(default='default content')),
                ('date', models.DateTimeField(default='default date')),
            ],
        ),
        migrations.AlterField(
            model_name='kessel',
            name='power',
            field=models.IntegerField(default='default power'),
        ),
    ]