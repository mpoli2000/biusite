# Generated by Django 4.1 on 2023-01-31 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdoku', '0006_alter_tablero_level_alter_tablero_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablero',
            name='user_sudoku',
            field=models.CharField(default='0', max_length=81),
        ),
        migrations.AlterField(
            model_name='tablero',
            name='size',
            field=models.CharField(choices=[('3', '3x3')], default='3', max_length=1),
        ),
    ]
