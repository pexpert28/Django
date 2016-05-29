from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class ShelegramUser(User):
    picture = models.ImageField(upload_to='/static/media/images/avatars/', default='/static/media/images/avatars/default.png', blank=True)
    User._meta.get_field('email').blank = False;
    def __str__(self):
        return self.username

        
class ShelegramGroup(models.Model):
    name = models.CharField(max_length=100, blank=False);
    admin = models.ForeignKey(ShelegramUser, on_delete=models.CASCADE, null=False, related_name='admin_user')
    picture = models.ImageField(upload_to='static/avatars/', default='static/avatars/default.jpg', blank=True)

    def __str__(self):
        return self.name
        
        
