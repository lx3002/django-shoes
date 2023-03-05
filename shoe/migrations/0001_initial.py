# Generated by Django 4.1.7 on 2023-03-04 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoes_name', models.CharField(max_length=30)),
                ('shoes_price', models.CharField(max_length=300)),
                ('shoes_image', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'shoe',
            },
        ),
    ]
