# Generated by Django 4.2.3 on 2023-07-20 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ulplataform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UplinkTheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_tema', models.CharField(max_length=20)),
                ('estilo', models.CharField(max_length=1000)),
            ],
        ),
    ]
