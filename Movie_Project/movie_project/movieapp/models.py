from django.db import models

class Movie(models.Model):
    name=models.charfield(max_length=250),
    desc=models.TextField(),
    year=models.IntegerField(),
    img=models.TextField(upload_to='gallery'),
    def __str__(self):
        return self.name
