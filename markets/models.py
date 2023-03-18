from django.db import models


class Market(models.Model):
    """
    Model for Markets Sushi Go took part.
    """
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='markets')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.name
