# Generated by Django 3.0.7 on 2020-06-30 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubumwe_app', '0004_loan'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='yarishyuwe',
            field=models.BooleanField(default=False),
        ),
    ]
