from django.db import models

class Client(models.Model):
# Client Model
    created_date = models.DateTimeField("created date")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    def __str__(self):
        return self.first_name + ' ' + self.last_name



