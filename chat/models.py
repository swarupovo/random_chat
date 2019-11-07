from django.contrib.auth.models import User
from django.db import models


# class userdata(models.Model):
#     CHOICE = (('M', 'MALE'),
#               ('F', 'FEMALE'))
#     username = models.CharField(max_length=50, blank=False, unique=True)
#     password = models.CharField(max_length=60, blank=False)
#     email_id = models.EmailField(max_length=50,blank=False)
#     gender = models.CharField(max_length=10, choices=CHOICE)
#
#     def __str__(self):
#         return self.username


class UserImage(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/profile_pic/', default='images/profile_pic/default.jpg')
    


