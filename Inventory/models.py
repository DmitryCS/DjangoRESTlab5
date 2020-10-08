from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from Player.models import Player


class ItemType(models.Model):
    # name = models.CharField(max_length=40, unique=True)
    type = models.CharField(max_length=40, unique=True)

    def __unicode__(self):
        return self.type


class Item(models.Model):
    itemType = models.ForeignKey(ItemType, null=True, on_delete=models.CASCADE) #models.CharField(ItemType)
    quality = models.SmallIntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    owner = models.ForeignKey(Player, null=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return "{0} - {1}".format(self.itemType,self.quality)