from django.db import models
from django.contrib.auth.models import User
from PIL import Image

WEEK_DAYS = (
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (7, 'Sunday'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics/')
    holiday = models.IntegerField(choices=WEEK_DAYS, default=7, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_image_url(self):
        try:
            return self.image.url
        except:
            return ''

    def get_appointments(self):
        try:
            return self.user.appointments.all().order_by('-date_created')
        except:
            return None


from .signals import *