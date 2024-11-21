from django.db import models
import os
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

def validate_audio_video_file(value):

    ext = os.path.splitext(value.name)[1].lower()
    # 这里对文件格式做判断
    allowed_audio_extensions = ['.mp3']
    allowed_video_extensions = ['.mp4', '.mov', '.avi', '.mkv']
    if ext not in allowed_audio_extensions + allowed_video_extensions:
        raise ValidationError(_('只允许上传MP3音频文件或常见视频格式文件（如MP4、MOV、AVI、MKV等）'))


class Music(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('audio', '音频'),
        ('video', '视频'),
    )
    name = models.CharField(max_length=200, verbose_name='音乐名')
    poster = models.ImageField(upload_to='media_posters/', verbose_name='媒体封面')
    media_file = models.FileField(upload_to='media_files/', verbose_name='媒体文件',
                                  validators=[validate_audio_video_file], default='',
                                  null=True)
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES, verbose_name='媒体类型'
                                  , default='未知',)
    lyrics = models.TextField(blank=True, null=True, verbose_name='歌词')

