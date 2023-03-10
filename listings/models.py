from django.db import models
from datetime import datetime
from realtors.models import Realtor
from tinymce import models as tinymce_models
from django.utils.html import mark_safe
from  embed_video.fields  import  EmbedVideoField
from ckeditor.fields import RichTextField
from django.db.models import UniqueConstraint
from django.db.models.functions import Upper
from django.contrib.auth import  get_user_model

User = get_user_model()

rating_choices = (
    (0,0),
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
)

class city(models.Model):
    title = models.CharField(max_length=200, unique=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "01. Society City"

class Society(models.Model):
    city = models.ForeignKey(city, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at= models.DateTimeField(auto_now_add=True, blank=True)
    updated_at= models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "02. Society Name"

class Society_Youtube_videos(models.Model):
    society = models.OneToOneField(Society, on_delete=models.CASCADE, default=None, unique=True)
    title = models.CharField(max_length=200)
    yut_video_1 = EmbedVideoField(blank=True,null=True)
    yut_video_2 = EmbedVideoField(blank=True,null=True)
    yut_video_3 = EmbedVideoField(blank=True,null=True)
    yut_video_4 = EmbedVideoField(blank=True,null=True)
    yut_video_5 = EmbedVideoField(blank=True,null=True)
    yut_video_6 = EmbedVideoField(blank=True,null=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at= models.DateTimeField(auto_now_add=True, blank=True)
    updated_at= models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'{self.society.title} Society Youtube Videos'

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
        verbose_name = "00. Owner Contact Us"

class Society_Home_Page_Images(models.Model):
    society = models.OneToOneField(Society, on_delete=models.CASCADE, default=None, unique=True)
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
        verbose_name = "17. Society Sector"

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
        verbose_name = "18. Society Phase and Sector"
        unique_together = ('society', 'society_phase','society_sector')

class Society_Phase_Youtube_videos(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, default=None)
    society_phase = models.ForeignKey(Socity_phase, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    yut_video_1 = EmbedVideoField(blank=True,null=True)
    yut_video_2 = EmbedVideoField(blank=True,null=True)
    yut_video_3 = EmbedVideoField(blank=True,null=True)
    yut_video_4 = EmbedVideoField(blank=True,null=True)
    yut_video_5 = EmbedVideoField(blank=True,null=True)
    yut_video_6 = EmbedVideoField(blank=True,null=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at= models.DateTimeField(auto_now_add=True, blank=True)
    updated_at= models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.society.title) + 'Society '+ str(self.society_phase.title)+' Youtube Videos'

    class Meta:
        verbose_name = "08. Society Phase Youtube Videos"
        unique_together = ('society', 'society_phase',)

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
        return f'{str(self.society.title)} Images of {str(self.society_phase.title)}'

    class Meta:
        verbose_name = "09. Society Phase Home Page Images"
        unique_together = ('society', 'society_phase',)

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
        verbose_name = "03. Society Status"

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

class Socity_transfer_office(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, default=None)
    society_phase = models.ForeignKey(Socity_phase, on_delete=models.CASCADE)
    office_name = models.CharField(max_length=200)
    office_contact_no = models.CharField(max_length=200)
    office_address = models.CharField(max_length=1000)
    description_and_details = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.office_name) +' '+str(self.society)+' '+str(self.society_phase)

    class Meta:
        verbose_name = "14. Society Transfer Office"

class Socity_Rating(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, default=None)
    society_phase = models.ForeignKey(Socity_phase, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=200)
    rate = models.IntegerField(choices=rating_choices, null=True, default=5)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.society.title) + ' and ' + str(self.society_phase.title) +' Rating'

    class Meta:
        verbose_name = "04. Society Rating"

class Listing(models.Model):
    socity_phase_sector = models.ForeignKey(Socity_phase_Sector, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    block = models.CharField(max_length=200, null=True)
    plot_no = models.CharField(max_length=200, null=True)
    description = RichTextField(blank=True, null=True)
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
        verbose_name = "19. Plot Listing"

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
        verbose_name = "15. Plot Detail Table Society Phase"

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
    transfer_charges = RichTextField(blank=True, null=True)
    transfer_office = models.CharField(max_length=2000)
    location_on_map = models.CharField(max_length=1000)
    society_location = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    download_location_file = models.FileField(upload_to='locationMap/%Y/%m/%d/', blank=True)
    official_website = models.CharField(max_length=1000)
    official_contact_number = models.CharField(max_length=1000)
    posession = models.BooleanField(default=False)
    posession_date = models.DateTimeField(default=datetime.now, blank=True)
    description_and_details_1 = RichTextField(blank=True, null=True)
    description_and_details_2 = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.society.title

    class Meta:
        verbose_name = "18. Society Detail Home Page"
        unique_together = ('society',)

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
    school_facilities = models.BooleanField(default=True)
    hospital_facilities = models.BooleanField(default=True)
    internt_facilities = models.BooleanField(default=True)
    telephone_facilities = models.BooleanField(default=True)
    club_facilities = models.BooleanField(default=True)
    transfer_charges = RichTextField(blank=True, null=True)
    transfer_office = models.CharField(max_length=2000)
    location_on_map = models.CharField(max_length=1000)
    society_location = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    official_website = models.CharField(max_length=1000)
    official_contact_number = models.CharField(max_length=1000)
    posession = models.CharField(max_length=2000)
    description_and_details_1 = RichTextField(blank=True, null=True)
    description_and_details_2 = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.society.title

    class Meta:
        verbose_name = "16. Society Phase Detail Home Page"
        unique_together=('society','society_phase')



class Socity_phase_maps(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, default=None)
    society_phase = models.ForeignKey(Socity_phase, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, blank=True)
    map = models.FileField(upload_to='locationMap/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.society.title) + 'and' + str(self.society_phase.title) +' Map'

    class Meta:
        verbose_name = "11. Society Phase Map"


class Socity_phase_other_documents_download(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, default=None)
    society_phase = models.ForeignKey(Socity_phase, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=5000, blank=True)
    document = models.FileField(upload_to='locationMap/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.society.title) + 'and' + str(self.society_phase.title) +' Download Other Documents'

    class Meta:
        verbose_name = "12. Society Phase Other Documents"


class Socity_phase_approved_from(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, default=None)
    society_phase = models.ForeignKey(Socity_phase, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.society.title) + 'and' + str(self.society_phase.title) +' Approved'

    class Meta:
        verbose_name = "13. Society Phase Approved"