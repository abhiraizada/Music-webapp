from django.db import models

# Create your models here.
class Album(models.Model):
    singer=models.CharField(max_length=30)
    singer_album=models.CharField(max_length=30)
    genre=models.CharField(max_length=30)
    def __str__(self):
        return self.singer + "---" + self.singer_album
class Song(models.Model):
    music=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=50)
    song_name=models.CharField(max_length=100)
    is_favorite=models.BooleanField(default=False)
    def __str__(self):
        return self.song_name