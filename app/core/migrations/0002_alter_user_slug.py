# Generated by Django 5.0.3 on 2024-04-02 07:07

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True),
        ),
    ]
