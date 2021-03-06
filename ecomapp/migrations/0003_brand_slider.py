# Generated by Django 3.2.4 on 2021-06-22 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0002_auto_20210621_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='products')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='products')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=100)),
            ],
        ),
    ]
