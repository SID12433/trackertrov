# Generated by Django 4.2.5 on 2024-05-08 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_adminapproved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hr',
            name='is_adminapproved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teamlead',
            name='is_adminapproved',
            field=models.BooleanField(default=False),
        ),
    ]