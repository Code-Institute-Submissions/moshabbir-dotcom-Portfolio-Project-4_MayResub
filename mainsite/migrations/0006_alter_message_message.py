# Generated by Django 3.2 on 2022-01-23 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_auto_20220120_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
