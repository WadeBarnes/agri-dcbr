# Generated by Django 2.2 on 2019-05-25 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regNum', models.CharField(max_length=10)),
                ('firstName', models.CharField(max_length=32)),
                ('middleName', models.CharField(max_length=32)),
                ('lastName', models.CharField(max_length=32)),
                ('slug', models.SlugField(blank=True, default='', max_length=32)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Operator')),
            ],
            options={
                'verbose_name_plural': 'Operators',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PRI', 'Primary'), ('LOC', 'Location'), ('VET', 'Veterinary')], default='PRI', max_length=3)),
                ('streetNum', models.IntegerField()),
                ('suite', models.CharField(blank=True, default='', max_length=32)),
                ('streetName', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('postalCode', models.CharField(max_length=7)),
                ('slug', models.SlugField(blank=True, default='', max_length=32)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('regNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.Operator')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]
