from django.db import models
from datetime import datetime
from tinymce import models as tinymce_models

class Contact(models.Model):
  listing = models.CharField(max_length=200)
  listing_id = models.IntegerField()
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)
  def __str__(self):
    return self.name



class Team_members(models.Model):
  name = models.CharField(max_length=200)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  is_mvp_team_member = models.BooleanField(default=False)
  description = models.CharField(max_length=2000, null=True)
  is_published = models.BooleanField(default=True, null=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  updated_at = models.DateTimeField(auto_now=True, blank=True)
  def __str__(self):
    return self.name

class About(models.Model):
  title = models.CharField(max_length=200)
  description = tinymce_models.HTMLField(blank=True)
  we_work_message = models.CharField(max_length=2000, null=True)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  updated_at = models.DateTimeField(auto_now=True, blank=True)
  def __str__(self):
    return str(self.title) + ' About'