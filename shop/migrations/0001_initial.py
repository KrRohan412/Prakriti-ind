# Generated by Django 4.1.7 on 2023-03-12 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=80)),
                ('product_desc', models.CharField(max_length=400)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
