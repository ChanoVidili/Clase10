# Generated by Django 4.2.3 on 2023-07-31 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('raza', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
