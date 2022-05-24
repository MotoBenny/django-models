from django.db import models
from django.contrib.auth import get_user_model


class Snack(models.Model):
    name = models.CharField(max_length=64)  # relational DB wants to know how much memory to allocate
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    # cascade means when the user goes away the data associated with the user goes away

    def __str__(self):
        return self.name  # so the name shows in the admin panel
