# Generated by Django 4.2.16 on 2024-12-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0003_remove_buyer_aga_buyer_age_buyer_balance_game_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='age',
            field=models.IntegerField(default='default age'),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='balance',
            field=models.DecimalField(decimal_places=2, default='default balance', max_digits=8),
        ),
        migrations.AlterField(
            model_name='game',
            name='cost',
            field=models.DecimalField(decimal_places=2, default='default cost', max_digits=8),
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(default='default description'),
        ),
        migrations.AlterField(
            model_name='game',
            name='size',
            field=models.IntegerField(default='default size'),
        ),
    ]