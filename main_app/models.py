from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
RATINGS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
)

class Place(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Review(models.Model):
    date = models.DateField('review date')
    details = models.CharField(max_length=500)
    rating = models.CharField(
        max_length=1,
        choices = RATINGS,
        default=RATINGS[0][0]
    )
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"{self.et"



# NEW COMMENTS FOR PULL REQUEST
# CHECK FOR PYCACHE
