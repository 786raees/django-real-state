from django.db import models
from datetime import datetime
from realtors.models import Realtor
from tinymce import models as tinymce_models
from django.utils.html import mark_safe

rating_choices = (
    (0,0),
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),

)
class city(models.Model):
    title = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "00. Society City"
class Society(models.Model):
    city = models.ForeignKey(city, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
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
        verbose_name = "01. Society Name"

    def img_preview(self):  # new
        return mark_safe('<img src = "{url}" width = "300"/>'.format(
            url=self.photo_main.url
        ))

class Society_Youtube_videos(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, default=None)
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
        verbose_name = "02. Society Youtube Videos"


class Owner_Contact_Us(models.Model):
    title = models.CharField(max_length=2000, blank=True)
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
        return str(self.title) +' Contacts Information'

    class Meta:
        verbose_name = "03. Owner Contact Us"
class Society_Home_Page_Images(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, default=None)
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
        verbose_name = "04. Society Home Page Images"

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
        verbose_name = "05. Plot Type"


class Plot_category(models.Model):
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "06. Plot Category"


class Socity_phase(models.Model):
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "07. Society Phase"

class Socity_Sector(models.Model):
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "12. Society Sector"
class Socity_phase_Sector(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, default=None)
    society_phase = models.ForeignKey(Socity_phase, on_delete=models.CASCADE)
    society_sector = models.ForeignKey(Socity_Sector, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.society) +' '+str(self.society_phase) + ' '+ str(self.society_sector)

    class Meta:
        verbose_name = "20. Society Phase and Sector"

class Society_Phase_Youtube_videos(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, default=None)
    society_phase = models.ForeignKey(Socity_phase, on_delete=models.CASCADE)
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
        return str(self.society.title) + 'Society '+ str(self.society_phase.title)+' Youtube Videos'

    class Meta:
        verbose_name = "08. Society Phase Youtube Videos"



class Society_Phase_Home_Page_Images(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, default=None)
    society_phase = models.ForeignKey(Socity_phase, on_delete=models.CASCADE)
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
        return str(self.society.title) + ' Images of '+ str(self.society_phase.title)

    class Meta:
        verbose_name = "09. Society Phase Home Page Images"

    def img_preview(self):  # new
        return mark_safe('<img src = "{url}" width = "300"/>'.format(
            url=self.photo_main.url
        ))

class Socity_latest_news(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, default=None)
    society_phase = models.ForeignKey(Socity_phase, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    news_link = models.CharField(max_length=1000, null=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.society.title) + 'and' + str(self.society_phase.title) +' Latest News'

    class Meta:
        verbose_name = "10. Society Latest News"

class Socity_Status(models.Model):
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "11. Society Status"



class Socity_tags(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "13. Society Tag"

class Socity_Rating(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, default=None)
    society_phase = models.ForeignKey(Socity_phase, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    rate = models.IntegerField(choices=rating_choices, null=True, default=5)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.society.title) + ' and ' + str(self.society_phase.title) +' Rating'

    class Meta:
        verbose_name = "14. Society Rating"
class Listing(models.Model):
    socity_phase_sector = models.ForeignKey(Socity_phase_Sector, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    block = models.CharField(max_length=200, null=True)
    plot_no = models.CharField(max_length=200, null=True)
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
        verbose_name = "15. Plot Listing"

class Plot_details_table(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE)
    dimension = models.CharField(max_length=200)
    plot_type = models.ForeignKey(Plot_types, on_delete=models.CASCADE)
    plot_category = models.ForeignKey(Plot_category, on_delete=models.CASCADE)
    society_phase = models.ForeignKey(Socity_phase, on_delete=models.CASCADE, null=True)
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
        verbose_name = "16. Plot Detail of Table Society"

class Plot_phase_details_table(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE)
    society_phase = models.ForeignKey(Socity_phase, on_delete=models.CASCADE)
    dimension = models.CharField(max_length=200)
    plot_type = models.ForeignKey(Plot_types, on_delete=models.CASCADE)
    plot_category = models.ForeignKey(Plot_category, on_delete=models.CASCADE)
    block = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    remarks = models.CharField(max_length=2000)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.society) +'Table' + str(self.society_phase)

    class Meta:
        verbose_name = "17. Plot Detail Table Society Phase"
class Society_details_home_page(models.Model):
    title = models.CharField(max_length=2000, blank=True)
    society = models.ForeignKey(Society, on_delete=models.CASCADE, default=None)
    society_youtube_videos = models.ForeignKey(Society_Youtube_videos, on_delete=models.CASCADE)
    society_home_page_images = models.ForeignKey(Society_Home_Page_Images, on_delete=models.CASCADE)
    plot_types = models.ForeignKey(Plot_types, on_delete=models.CASCADE)
    society_status = models.ForeignKey(Socity_Status, on_delete=models.CASCADE)
    launch_date = models.DateTimeField(default=datetime.now, blank=True)
    approvals = models.CharField(max_length=1000)
    facilities = models.CharField(max_length=2000)
    transfer_charges = models.CharField(max_length=2000)
    transfer_office = models.CharField(max_length=2000)
    location_on_map = models.CharField(max_length=1000)
    society_location = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    download_location_file = models.CharField(max_length=1000)
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
        verbose_name = "18. Society Detail Home Page"

    def img_preview(self):  # new
        return mark_safe('<img src = "{url}" width = "300"/>'.format(
            url=self.society_location.url
        ))



class Society_phase_details_home_page(models.Model):
    title = models.CharField(max_length=2000, blank=True)
    society = models.ForeignKey(Society, on_delete=models.CASCADE, default=None)
    society_phase_youtube_videos = models.ForeignKey(Society_Phase_Youtube_videos, on_delete=models.CASCADE)
    society_phase_home_page_images = models.ForeignKey(Society_Phase_Home_Page_Images, on_delete=models.CASCADE)
    plot_types = models.ForeignKey(Plot_types, on_delete=models.CASCADE)
    society_status = models.ForeignKey(Socity_Status, on_delete=models.CASCADE)
    society_phase = models.ForeignKey(Socity_phase, on_delete=models.CASCADE, null=True)
    launch_date = models.DateTimeField(default=datetime.now, blank=True)
    approvals = models.CharField(max_length=1000)
    gas_facilities = models.BooleanField(default=True)
    water_facilities = models.BooleanField(default=True)
    mantaince_facilities = models.BooleanField(default=True)
    secuirty_facilities = models.BooleanField(default=True)
    sav_facilities = models.BooleanField(default=True)
    electricity_facilities = models.BooleanField(default=True)
    transfer_charges = models.CharField(max_length=2000)
    transfer_office = models.CharField(max_length=2000)
    location_on_map = models.CharField(max_length=1000)
    society_location = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    download_location_file = models.CharField(max_length=1000)
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
        verbose_name = "19. Society Phase Detail Home Page"

    def img_preview(self):  # new
        return mark_safe('<img src = "{url}" width = "300"/>'.format(
            url=self.society_location.url
        ))