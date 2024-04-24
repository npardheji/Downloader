from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    youtube_url = models.URLField()

class VideoResolution(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    resolution = models.CharField(max_length=10)  # 360p, 720p, 1080p
    size_in_mb = models.FloatField()
    download_link = models.URLField()