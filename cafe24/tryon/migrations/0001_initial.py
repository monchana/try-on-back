# Generated by Django 3.1 on 2021-07-28 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Models',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='models')),
            ],
            options={
                'verbose_name': 'Image_models',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products')),
                ('part', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TemplatePage',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=200)),
                ('part', models.CharField(max_length=50)),
                ('single_line', models.TextField()),
                ('grid', models.TextField()),
                ('zigzag', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TryOnImage',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='adjusted')),
                ('default', models.BooleanField(default=False)),
                ('template', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='tryon.templatepage')),
            ],
        ),
        migrations.CreateModel(
            name='ProductNB',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='background_crop')),
                ('title', models.CharField(max_length=200)),
                ('part', models.CharField(max_length=50)),
                ('product', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='tryon.product')),
            ],
        ),
    ]
