# Generated by Django 4.2.4 on 2023-08-02 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvdrental', '0002_rental_renewal_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='renewal',
            old_name='rental_id',
            new_name='rental',
        ),
    ]
