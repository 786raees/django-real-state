from django.db import models
from datetime import datetime
from realtors.models import Realtor
from tinymce import models as tinymce_models
from django.utils.html import mark_safe

class Society(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at= models.DateTimeField(auto_now_add=True, blank=True)
    updated_at= models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "1. Society Name"

    def img_preview(self):  # new
        return mark_safe('<img src = "{url}" width = "300"/>'.format(
            url=self.photo_main.url
        ))

class Society_Youtube_videos(models.Model):
    society = models.ForeignKey(Society, on_delete=models.DO_NOTHING, default=None)
    title = models.CharField(max_length=200)
    yut_video_1 = models.CharField(max_length=2000, blank=True)
    yut_video_2 = models.CharField(max_length=2000, blank=True)
    yut_video_3 = models.CharField(max_length=2000, blank=True)
    yut_video_4 = models.CharField(max_length=2000, blank=True)
    yut_video_5 = models.CharField(max_length=2000, blank=True)
    yut_video_6 = models.CharField(max_length=2000, blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at= models.DateTimeField(auto_now_add=True, blank=True)
    updated_at= models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.society.title) + 'Society Youtube Videos'

    class Meta:
        verbose_name = "2. Society Youtube Videos"

class Society_Contact_Us(models.Model):
    society = models.ForeignKey(Society, on_delete=models.DO_NOTHING, default=None)
    location = models.CharField(max_length=2000, blank=True)
    phone_number = models.CharField(max_length=2000, blank=True)
    Mobile_number = models.CharField(max_length=2000, blank=True)
    whatsapp_number = models.CharField(max_length=2000, blank=True)
    fb_id = models.CharField(max_length=2000, blank=True)
    instagram_id = models.CharField(max_length=2000, blank=True)
    gmail_id = models.CharField(max_length=2000, blank=True)
    linkedin_id = models.CharField(max_length=2000, blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at= models.DateTimeField(auto_now_add=True, blank=True)
    updated_at= models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.society.title) +' Contacts Information'

    class Meta:
        verbose_name = "3. Society Contact Us"
class Society_Home_Page_Images(models.Model):
    society = models.ForeignKey(Society, on_delete=models.DO_NOTHING, default=None)
    title = models.CharField(max_length=200)
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
    created_at= models.DateTimeField(auto_now_add=True, blank=True)
    updated_at= models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.society.title) + ' Images'

    class Meta:
        verbose_name = "4. Society Home Page Images"

    def img_preview(self):  # new
        return mark_safe('<img src = "{url}" width = "300"/>'.format(
            url=self.photo_main.url
        ))


class Plot_types(models.Model):
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "5. Plot Type"


class Plot_category(models.Model):
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "6. Plot Category"


class Socity_phase(models.Model):
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "7. Society Phase"

class Socity_latest_news(models.Model):
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "8. Society Latest News"

class Socity_Status(models.Model):
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "9. Society Status"


class Listing(models.Model):
    society = models.ForeignKey(Society, on_delete=models.DO_NOTHING, default=None)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    description = tinymce_models.HTMLField(blank=True)
    video_url = models.CharField(max_length=1000, null=True)
    price = models.IntegerField(null=True)
    bedrooms = models.IntegerField(null=True)
    bathrooms = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    garage = models.IntegerField(default=0)
    square_foot = models.IntegerField(null=True)
    plot_size = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "7. Plot Listing"

class Plot_details_table(models.Model):
    society = models.ForeignKey(Society, on_delete=models.DO_NOTHING)
    society_phase = models.ForeignKey(Socity_phase, on_delete=models.DO_NOTHING)
    dimension = models.CharField(max_length=200)
    plot_type = models.ForeignKey(Plot_types, on_delete=models.DO_NOTHING)
    plot_category = models.ForeignKey(Plot_category, on_delete=models.DO_NOTHING)
    block = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    remarks = models.CharField(max_length=2000)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.society) +'Table'

    class Meta:
        verbose_name = "5. Plot Detail of Table Society"


class Society_details_home_page(models.Model):
    society = models.ForeignKey(Society, on_delete=models.DO_NOTHING, default=None)
    plot_details_table = models.ForeignKey(Plot_details_table, on_delete=models.DO_NOTHING)
    society_youtube_videos = models.ForeignKey(Society_Youtube_videos, on_delete=models.DO_NOTHING)
    society_home_page_images = models.ForeignKey(Society_Home_Page_Images, on_delete=models.DO_NOTHING)
    society_contact_us = models.ForeignKey(Society_Contact_Us, on_delete=models.DO_NOTHING)
    plot_types = models.ForeignKey(Plot_types, on_delete=models.DO_NOTHING)
    society_status = models.ForeignKey(Socity_Status, on_delete=models.DO_NOTHING)
    rating = models.CharField(max_length=200)
    launch_date = models.CharField(max_length=1000)
    approvals = models.CharField(max_length=1000)
    facilities = models.CharField(max_length=2000)
    transfer_charges = models.CharField(max_length=2000)
    transfer_office = models.CharField(max_length=2000)
    location_on_map = models.CharField(max_length=1000)
    society_location = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    official_website = models.CharField(max_length=1000)
    official_contact_number = models.CharField(max_length=1000)
    posession = models.BooleanField(default=False)
    posession_date = models.DateTimeField(default=datetime.now, blank=True)
    description_and_details_1 = tinymce_models.HTMLField(blank=True)
    description_and_details_2 = tinymce_models.HTMLField(blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.society.title

    class Meta:
        verbose_name = "6. Society Detail Home Page"

    def img_preview(self):  # new
        return mark_safe('<img src = "{url}" width = "300"/>'.format(
            url=self.society_location.url
        ))
