# Generated by Django 5.0.3 on 2024-03-26 11:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_prise',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='client',
            name='client_registration_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_added_date',
        ),
        migrations.AddField(
            model_name='client',
            name='registration_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='added_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
