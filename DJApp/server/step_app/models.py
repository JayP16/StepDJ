from django.db import models

# Create your models here.
class StepUser(models.Model):
    userEmail = models.CharField(max_length=100)	
    userName = models.CharField(max_length=30)

    def __str__(self):
        return self.userName+" "+self.userEmail
