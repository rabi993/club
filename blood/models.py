from django.db import models
from django.contrib.auth.models import User
from people.models import People  # Import the People model if it's in the same app

# Create your models here.
class Blood(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the User model
    person = models.ForeignKey(People, on_delete=models.CASCADE)  # Link to the People model
    
    last_donate_date = models.DateField(blank=True, null=True)  # Date of the last blood donation

    @property
    def blood_group(self):
        # Fetch the blood group from the related People model
        return self.person.blood_group if self.person else None
    def __str__(self):
        return f"{self.user.username} - {self.person.blood_group}"

    class Meta:
        verbose_name = "Blood"
        verbose_name_plural = "Bloods"
        ordering = ['-last_donate_date']  # Most recent donors first
