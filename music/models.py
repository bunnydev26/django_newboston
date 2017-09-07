from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return "{0} - {1}".format(self.album_title, self.artist)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    file_type = models.CharField(max_length=10)

    def __str__(self):
        return self.song_title