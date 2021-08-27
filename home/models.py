from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	birthday = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='home/%Y/%m/%d', blank=True)

	def __str__(self):
		return f'Profile for user {self.user.username}'

	@property
	def get_photo_url(self):
		if self.photo and hasattr(self.photo, 'url'):
			return self.photo.url
		else:
			return 'https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png'