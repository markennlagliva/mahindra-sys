# Generated by Django 4.2.3 on 2023-10-19 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('timein', models.TimeField()),
                ('timeout', models.TimeField()),
            ],
        ),
    ]
