# Generated by Django 3.0.8 on 2020-07-25 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qcrep', '0008_auto_20200725_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qcreport',
            name='aspect',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='qcreport',
            name='client',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='qcreport',
            name='framesPerSecond',
            field=models.CharField(choices=[('Pending', 'Pending'), ('23.98P', '23.98 Progressive'), ('23.98I', '23.98 Interlaced'), ('29.97P', '29.97 Progressive'), ('29.97I', '29.97 Interlaced'), ('25P', '25 Progressive'), ('25I', '25 Interlaced'), ('24P', '24 Progressive'), ('59.94I', '59.94I')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='qcreport',
            name='missing_elements',
            field=models.CharField(choices=[('MovieTitle', 'Movie Title'), ('Initial Credits', 'Initial Credits'), ('Final Roller', 'Final Roller'), ('Ep Num', 'Episode Number'), ('None', 'None'), ('Pending', 'Pending')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='qcreport',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='qcreport',
            name='tecreject',
            field=models.CharField(choices=[('Pending', 'Pending'), ('MB', 'Macroblocks'), ('IF', 'Inverted Fields'), ('BF', 'Blended Fields'), ('BM', 'Broken Media'), ('VBI', 'VBI Line'), ('Sync', 'Out of sync'), ('RG', 'Red or Green Frames'), ('FF', 'Frezzed Frames'), ('RF', 'Repeated Frames'), ('AF', 'Artifacts'), ('SA', 'Saturated Audio'), ('WAM', 'Audio does not belong to media'), ('AN', 'Audio Noise'), ('Drop', 'Audio/Video Drop Out'), ('BR', 'Low Bit Rate'), ('VS', 'Video out or range or Standards'), ('None', 'None')], default='Pending', max_length=100),
        ),
    ]