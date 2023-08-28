from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import *
from home.models import *
from django.contrib import messages
from django.shortcuts import render

@receiver(user_logged_in, sender = User)
def login_success(sender, request, user, **kwargs):
  #  messages.success(user, "has logged in successfully")
    print(user, "has logged in successfully")

#user_logged_in.connect(login_success)


@receiver(pre_save, sender = Car)
def pre_save_car(sender, instance, **kwargs):
    print(sender, "is going to be stored")
# messages.success(instance, "has been saved")
# Note that instance contains the __str__ return type
    print(instance, " has been saved")
    