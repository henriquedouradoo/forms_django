# Generated by Django 4.2.4 on 2023-08-10 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuarios', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('texto', models.TextField(max_length=350)),
            ],
        ),
    ]
