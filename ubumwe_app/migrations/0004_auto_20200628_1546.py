# Generated by Django 3.0.7 on 2020-06-28 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubumwe_app', '0003_auto_20200628_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='contributions',
            field=models.ManyToManyField(related_name='_member_contributions_+', to='ubumwe_app.Contribution'),
        ),
        migrations.AlterField(
            model_name='member',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]