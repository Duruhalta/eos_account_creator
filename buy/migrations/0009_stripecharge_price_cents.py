# Generated by Django 2.0.6 on 2018-06-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0008_auto_20180619_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripecharge',
            name='price_cents',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]