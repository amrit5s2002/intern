# Generated by Django 4.1.3 on 2022-11-09 16:01

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
                ('Product_Name', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('Quantity', models.IntegerField()),
            ],
        ),
    ]
