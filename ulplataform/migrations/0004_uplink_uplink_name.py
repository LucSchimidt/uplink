# Generated by Django 4.2.3 on 2023-08-03 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ulplataform', '0003_uplink_tema'),
    ]

    operations = [
        migrations.AddField(
            model_name='uplink',
            name='uplink_name',
            field=models.CharField(default='defaul-item', max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
