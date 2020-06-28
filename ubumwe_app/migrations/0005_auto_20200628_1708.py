# Generated by Django 3.0.7 on 2020-06-28 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ubumwe_app', '0004_auto_20200628_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='contributions',
        ),
        migrations.AlterField(
            model_name='contribution',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributions', to='ubumwe_app.Member'),
        ),
    ]