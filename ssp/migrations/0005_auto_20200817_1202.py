# Generated by Django 3.0.7 on 2020-08-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssp', '0004_auto_20200817_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nist_control_parameter',
            name='param_class',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='nist_control_parameter',
            name='param_depends_on',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='nist_control_parameter',
            name='param_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='nist_control_parameter',
            name='param_text',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='nist_control_parameter',
            name='param_type',
            field=models.CharField(choices=[('label', 'Label'), ('description', 'Description'), ('constraint', 'Constraint'), ('guidance', 'Guidance'), ('value', 'Value'), ('select', 'Select')], max_length=255),
        ),
    ]
