# Generated by Django 3.0.7 on 2021-11-02 21:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(default=5000),
            preserve_default=False,
        ),
    ]
