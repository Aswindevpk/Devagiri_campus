# Generated by Django 4.2 on 2023-04-12 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_fests_logo_fests_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ImageField(upload_to='carousel_images/'),
        ),
    ]
