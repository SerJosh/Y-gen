# Generated by Django 5.0.6 on 2024-06-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='heading_update',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
