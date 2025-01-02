from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)  # Name of the event (increased max_length for flexibility)
    description = models.TextField()  # Detailed description of the event
    image = models.URLField(max_length=500, blank=True, null=True)  # Optional URL for an event image
    held_on = models.DateTimeField()  # Date and time when the event is held

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['-held_on']  # Orders events by most recent first
