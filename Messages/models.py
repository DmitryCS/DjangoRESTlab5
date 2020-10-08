from django.db import models
from Player.models import Player


# Create your models here.
class Message(models.Model):
    playerFrom = models.ForeignKey(Player, null=False, related_name='playerFrom', on_delete=models.CASCADE)
    playerTo = models.ForeignKey(Player, null=False, related_name='playerTo', on_delete=models.CASCADE)
    messageText = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.messageText