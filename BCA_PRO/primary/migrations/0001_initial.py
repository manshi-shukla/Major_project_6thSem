# Generated by Django 5.0.3 on 2024-03-12 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registered_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('donor', 'Donor'), ('recipient', 'Recipient')], max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('pincode', models.CharField(max_length=6)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]