from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class ShelegramUser(User):
    picture = models.ImageField(upload_to='static/avatars/', default='static/avatars/default.jpg', blank=True)
    User._meta.get_field('email').blank = False;
    def __str__(self):
        return self.username;