from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    membersAge = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Level(models.Model):
    firstname = models.ForeignKey(Member, on_delete=models.CASCADE)
    danLevel = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.firstname}: {self.danLevel}"