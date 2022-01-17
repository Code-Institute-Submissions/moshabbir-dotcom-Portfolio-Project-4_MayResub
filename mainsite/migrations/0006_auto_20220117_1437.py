# Generated by Django 3.2 on 2022-01-17 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_booking_treatment'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='message',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='addinfo',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='treatment',
            field=models.CharField(choices=[('physical_therapy', 'Physical Therapy -£45'), ('sports_massage_therapy', 'Sports Massage Therapy -£45'), ('fire_cupping_therapy', 'Fire Cupping Therapy -£50'), ('swedish_massage_therapy', 'Swedish Massage Therapy -£45'), ('aroma_therapy', 'Aromatherapy -£45'), ('wet_cupping_therapy', 'Wet Cupping Therapy -£45'), ('graston_therapy', 'Graston IATM Therapy -£45'), ('nutrition_therapy', 'Nutritional Therapy -£45')], default='Physical Therapy -£45', max_length=100),
        ),
    ]
