# Generated by Django 4.1.7 on 2023-07-04 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_course_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='community',
            old_name='full_form',
            new_name='about',
        ),
        migrations.RenameField(
            model_name='fests',
            old_name='full_form',
            new_name='about',
        ),
    ]
