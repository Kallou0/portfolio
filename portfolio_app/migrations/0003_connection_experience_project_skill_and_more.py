# Generated by Django 4.2.1 on 2023-05-17 22:17

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_customuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=500)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True)),
                ('is_present', models.BooleanField(blank=True, null=True)),
                ('responsibilities_1', models.CharField(blank=True, default=None, max_length=2000)),
                ('responsibilities_2', models.CharField(blank=True, default=None, max_length=2000)),
                ('responsibilities_3', models.CharField(blank=True, default=None, max_length=2000)),
                ('responsibilities_4', models.CharField(blank=True, default=None, max_length=2000)),
                ('company', models.CharField(blank=True, default=None, max_length=200)),
                ('location', models.CharField(blank=True, default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=2000)),
                ('github_link', models.CharField(max_length=2000)),
                ('tech_stack', models.CharField(max_length=500)),
                ('image', models.FilePathField(default='', path='C:\\Users\\marshal.nzenza\\Documents\\projects\\sidegig\\portfolio\\portfolio_app/static/img')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='designation',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
