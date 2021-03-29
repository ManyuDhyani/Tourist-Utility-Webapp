from django.db import models

class City(models.Model):
    city = models.CharField(max_length=50)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city