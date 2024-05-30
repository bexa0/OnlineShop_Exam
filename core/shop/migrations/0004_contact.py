# Generated by Django 4.2.13 on 2024-05-30 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_cartitem_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_shop', models.CharField(max_length=55)),
                ('location', models.CharField(max_length=255)),
                ('phone', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
    ]
