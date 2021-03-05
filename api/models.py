from django.db import models

RATE_CHOICES=(
    ('5','5 Stars'),
    ('4','4 Stars'),
    ('3','3 Stars'),
    ('2','2 Stars'),
    ('1','1 Stars'),
    ('N/A','N/A'),
)

TYPE=(
    ('movie','movie'),
    ('series','series'),
    ('episode','episode'),
)

class Movie(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    created=models.DateField()
    rated=models.CharField(choices=RATE_CHOICES,max_length=4)
    duration=models.CharField(max_length=10)
    genre=models.ForeignKey('Genre',on_delete=models.SET_NULL,null=True,blank=True)
    actors=models.TextField()
    country=models.CharField(max_length=200)
    type=models.CharField(choices=TYPE,max_length=10)
    poster=models.ImageField()
    director=models.CharField(max_length=250)
    language=models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.title


class Genre(models.Model):
    name=models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name
    
