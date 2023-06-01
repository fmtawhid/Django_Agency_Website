from django.db import models

# Create your models here.
class offerOrder(models.Model):
    need = models.CharField(max_length=200)
    package = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    mail = models.EmailField()
    sms = models.CharField(max_length=500)

    def __str__(self):
        return self.name