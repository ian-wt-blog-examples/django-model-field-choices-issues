# Generated by Django 5.2.1 on 2025-05-28 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('JR', 'Junior'), ('SO', 'Sophomore'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2),
        ),
    ]
