# Generated by Django 3.0.7 on 2020-06-13 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubumwe_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('PR', 'President'), ('VP', 'Vice President'), ('CO', 'Comptable'), ('UM', 'Umwanditsi'), ('JY', 'Umujyanama'), ('MB', 'Member')], max_length=2),
        ),
    ]