# Generated by Django 4.2.3 on 2023-09-05 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_registered_lastname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registered',
            old_name='userId',
            new_name='userid',
        ),
    ]
