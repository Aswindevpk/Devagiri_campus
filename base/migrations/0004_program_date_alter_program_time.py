# Generated by Django 4.2 on 2023-04-08 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]