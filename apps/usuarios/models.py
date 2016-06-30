from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, unique=True)
    email = models.EmailField()
    TIPO_CHOICES = (
        ("ScrumMember", 'ScrumMember'),
        ("TeamMember", 'TeamMember'),
    )
    rol = models.CharField(max_length=1, choices=TIPO_CHOICES, default="TeamMember")

    def __unicode__(self):
    	return self.user.username
