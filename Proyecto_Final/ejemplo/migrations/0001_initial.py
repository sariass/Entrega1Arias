# Generated by Django 4.1.3 on 2022-11-30 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('f_nacimiento', models.IntegerField()),
                ('numero_pasaporte', models.IntegerField()),
                ('edad', models.IntegerField())
                
            ],
        ),
    ]
