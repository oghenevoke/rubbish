from django.db import models


class Contactus(models.Model):
    fname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    msg_date = models.DateTimeField()

    def __str__(self):
        var = self.fname
        return var
