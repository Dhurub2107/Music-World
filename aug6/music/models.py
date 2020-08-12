from django.db import models
import django.core.urlresolvers

def image_val(value):
    if not(value.name.endswith(".jpg")or value.name.endswith(".png")):
        raise ValueError("Invalid Image")
def song_val(value):
    if not(value.name.endswith(".mp3")or value.name.endswith(".aac")):
        raise ValueError("Invalid File")

class Album(models.Model):
    title=models.CharField(max_length=100)
    artist=models.CharField(max_length=100)
    genre=models.CharField(max_length=50)
    a_logo = models.FileField(validators=[image_val])
    def get_absolute_url(self):
        return reverse('music:song',kwargs={"pk":self.id})


    def __str__(self):
        return "Album: "+self.title+" artist:"+self.artist


class Song(models.Model):
    aid=models.ForeignKey(Album,on_delete=models.CASCADE)
    stitle=models.CharField(max_length=100)
    filetype=models.CharField(max_length=50)
    sartist=models.CharField(max_length=100)
    file=models.FileField(validators=[song_val])
    def __str__(self):
        return "Song: " + self.stitle + " artist:" + self.sartist

    def get_absolute_url(self):
        return reverse('music:song', kwargs={"pk": self.aid.id})