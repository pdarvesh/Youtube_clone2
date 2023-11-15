from django.db import models
from taggit.managers import TaggableManager


from django.conf import settings
from core.models import user_directory_path

User = settings.AUTH_USER_MODEL

STATUS =  (
    ("active", "Active"),
    ("disable", "Disable"),

)

# Create your models here.
# def user_directory_path(instance, filename):
#     return "user_{0}/{1}".format(instance.user.id, filename) 

class Channel(models.Model):
    channel_art = models.ImageField(upload_to=user_directory_path, null=True, blank=True, default="channel-art.jpg")
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    full_name = models.CharField(max_length=200) 
    channel_name = models.CharField(max_length=200) 
    description = models.TextField(null=True, blank=True)
    keywords = TaggableManager()
    joined = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=100, default="active")
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="channel")
    subscribers = models.ManyToManyField(User, related_name="user_subs")
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.channel_name


