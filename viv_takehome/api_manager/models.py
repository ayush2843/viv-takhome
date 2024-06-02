from django.db import models


class PlaylistData(models.Model):
    index = models.IntegerField(primary_key=True)
    id = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    danceability = models.FloatField()
    energy = models.FloatField()
    key = models.IntegerField()
    loudness = models.FloatField()
    mode = models.IntegerField()
    acousticness = models.FloatField()
    instrumentalness = models.FloatField()
    liveness = models.FloatField()
    valence = models.FloatField()
    tempo = models.FloatField()
    duration_ms = models.IntegerField()
    time_signature = models.IntegerField()
    num_bars = models.IntegerField()
    num_sections = models.IntegerField()
    num_segments = models.IntegerField()
    class_field = models.IntegerField()
    star_rating = models.FloatField(null=True)

    def __str__(self):
        return self.title
