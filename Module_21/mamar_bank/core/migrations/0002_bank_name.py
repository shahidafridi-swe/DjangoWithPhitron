# Generated by Django 5.0.6 on 2024-07-03 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
