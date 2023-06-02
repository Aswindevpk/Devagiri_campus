# Generated by Django 4.2 on 2023-04-08 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_fests_blooddonation'),
    ]

    operations = [
        migrations.AddField(
            model_name='fests',
            name='logo',
            field=models.ImageField(default='default_image.jpg', upload_to='fest_logos'),
        ),
        migrations.AddField(
            model_name='fests',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
