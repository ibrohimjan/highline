from django.db import models


class HomeVideo(models.Model):
    name = models.CharField("name", max_length=256)
    description = models.TextField("description")
    video = models.FileField("video", upload_to="home_video/%Y/%m")


    class Meta:
        db_table = "home_video"
        verbose_name = ("home video")
        verbose_name_plural = ("home videos")

    def __str__(self):
        return f"{self.name}"


