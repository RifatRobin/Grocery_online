# Generated by Django 3.1.3 on 2021-10-17 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=30)),
                ('productDescription', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('currency', models.CharField(choices=[('taka', 'taka'), ('rupe', 'rupe')], default='taka', max_length=6)),
                ('madeDate', models.DateField()),
                ('expireDate', models.DateField()),
                ('status_of_product', models.CharField(choices=[('In stock', 'In stock'), ('Out of stock', 'Out of stock')], default='In stock', max_length=15)),
            ],
        ),
    ]
