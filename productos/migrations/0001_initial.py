# Generated by Django 2.0.2 on 2018-03-02 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('is_variation', models.BooleanField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField()),
                ('type', models.CharField(max_length=100)),
                ('brand_id', models.IntegerField()),
                ('code', models.IntegerField()),
                ('family', models.IntegerField()),
                ('is_complement', models.BooleanField()),
                ('is_delete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductsDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('is_visibility', models.BooleanField()),
                ('price', models.FloatField()),
                ('price_offer', models.FloatField()),
                ('offer_day_from', models.DateTimeField()),
                ('offer_day_to', models.DateTimeField()),
                ('quantity', models.IntegerField()),
                ('sku', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Products')),
            ],
        ),
    ]