# Generated by Django 3.1.7 on 2021-03-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='created',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(max_length=10),
        ),
    ]
