# Generated by Django 3.0.8 on 2020-07-25 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qcrep', '0010_qcreport_qc_duedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qcreport',
            name='image',
            field=models.ImageField(default='image_penging.png', upload_to='qcreports_pics'),
        ),
    ]
