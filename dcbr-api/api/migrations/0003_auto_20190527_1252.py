# Generated by Django 2.2 on 2019-05-27 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_address_operator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='category',
        ),
        migrations.AlterField(
            model_name='address',
            name='type',
            field=models.CharField(choices=[('PRI', 'Primary'), ('OPN', 'Operation'), ('VET', 'Veterinary')], default='PRI', max_length=3),
        ),
        migrations.AlterField(
            model_name='operator',
            name='lastName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='operator',
            name='middleName',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
