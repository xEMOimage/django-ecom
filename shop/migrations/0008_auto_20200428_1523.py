# Generated by Django 3.0.5 on 2020-04-28 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
