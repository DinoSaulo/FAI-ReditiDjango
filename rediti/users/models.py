from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from common.models import IndexedTimeStampedModel
from .manager import UserManager

class User(AbstractBaseUser, PermissionsMixin, IndexedTimeStampedModel):
    email = models.EmailField("E-mail",unique=True)
    userame = models.CharField("Nome do usuário",max_length = 30, unique = True)
    description = models.TextField("Descrição",blank=True)
    karma = models.IntegerField(default=0)
    avatar = models.ImageField(blank=True, default = 'veigão.jpeg')
    is_staff = models.BooleanField("O boy é STAFF?",default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.userame

