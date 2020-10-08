from django.db import models

Location_type = (
    ('Forest', u'Forest'),
    ('Desert', u'Desert'),
    ('Dungeon', u'Dungeon'),
    ('River', u'River'),
    ('Ocean', u'Ocean'),
)


class Location(models.Model):
    locationId = models.CharField(verbose_name=u'Location Id', max_length=10, unique=True,
                                  default='0-0')
    description = models.TextField(verbose_name=u'Location Description', blank=True)
    locationType = models.CharField(verbose_name=u'Location Type', max_length=15,
                                    choices=Location_type, default='Forest')

    def __unicode__(self):
        return self.locationId

    def __str__(self):
        return self.locationId