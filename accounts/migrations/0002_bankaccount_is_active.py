# Generated by Django 5.1 on 2024-08-08 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='is_active',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
