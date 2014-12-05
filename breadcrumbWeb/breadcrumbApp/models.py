from django.db import models

class Project(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Wave(models.Model):
    name = models.CharField(max_length = 50)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name

class Shop(models.Model):
    shopName = models.CharField(max_length = 100)
    district = models.CharField(max_length = 3)
    wave = models.ForeignKey(Wave)

    def __str__(self):
        return self.shopName + " (" + self.district + ")"
    
