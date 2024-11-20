# Generated by Django 4.2.16 on 2024-11-20 09:11

from django.db import migrations, models
import musicapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_alter_music_media_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='media_file',
            field=models.FileField(default='', null=True, upload_to='media_files/', validators=[musicapp.models.validate_audio_video_file], verbose_name='媒体文件'),
        ),
    ]
