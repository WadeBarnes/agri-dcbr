# Generated by Django 2.2 on 2019-09-10 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20190821_2018'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Registration_Number',
            new_name='Registration',
        ),
        migrations.AlterModelOptions(
            name='registration',
            options={'verbose_name': 'new registration', 'verbose_name_plural': 'Registrations'},
        ),
        migrations.RenameField(
            model_name='address',
            old_name='registration_Number',
            new_name='registration_number',
        ),
        migrations.RenameField(
            model_name='animal_risk_factor',
            old_name='registration_Number',
            new_name='registration_number',
        ),
        migrations.RenameField(
            model_name='association_membership',
            old_name='registration_Number',
            new_name='registration_number',
        ),
        migrations.RenameField(
            model_name='inspection',
            old_name='registration_Number',
            new_name='registration_number',
        ),
        migrations.RenameField(
            model_name='operation_risk_factor',
            old_name='registration_Number',
            new_name='registration_number',
        ),
        migrations.RenameField(
            model_name='operator',
            old_name='registration_Number',
            new_name='registration_number',
        ),
    ]
