# Generated by Django 3.0.5 on 2020-04-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200426_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('watch', 'watch'), ('Book', 'Book'), ('Clothes', 'Clothes'), ('Electronic', 'Electronic')], max_length=50, null=True),
        ),
    ]
