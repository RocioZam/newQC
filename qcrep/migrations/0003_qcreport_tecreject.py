# Generated by Django 2.0.2 on 2020-07-16 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qcrep', '0002_qcreport_framespersecond'),
    ]

    operations = [
        migrations.AddField(
            model_name='qcreport',
            name='tecreject',
            field=models.CharField(choices=[('MB', 'Macroblocks'), ('IF', 'Inverted Fields'), ('BF', 'Blended Fields'), ('BM', 'Broken Media'), ('VBI', 'VBI Line'), ('Sync', 'Out of sync'), ('RG', 'Red or Green Frames'), ('FF', 'Frezzed Frames'), ('RF', 'Repeated Frames'), ('AF', 'Artifacts'), ('SA', 'Saturated Audio'), ('WAM', 'Audio does not belong to media'), ('AN', 'Audio Noise'), ('Drop', 'Audio/Video Drop Out'), ('BR', 'Low Bit Rate'), ('VS', 'Video out or range or Standards')], default='VB', max_length=100),
        ),
    ]
