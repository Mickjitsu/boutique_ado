# Generated by Django 5.1.4 on 2025-01-06 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='default name', max_length=254),
            preserve_default=False,
        ),
    ]