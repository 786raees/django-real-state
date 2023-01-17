from django.db import models
from datetime import datetime
from realtors.models import Realtor


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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "1. Society Name"


class Listing(models.Model):
    society = models.ForeignKey(Society, on_delete=models.DO_NOTHING, default=None)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=20, null=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(null=True)
    bedrooms = models.IntegerField(null=True)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField(null=True)
    lot_size = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "7. Plot Listing"


class Plot_types(models.Model):
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "3. Plot Type"


class Plot_category(models.Model):
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "4. Plot Category"


class Socity_phase(models.Model):
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "2. Society Phase"


class Plot_details_table(models.Model):
    society = models.ForeignKey(Society, on_delete=models.DO_NOTHING)
    society_phase = models.ForeignKey(Socity_phase, on_delete=models.DO_NOTHING)
    dimension = models.CharField(max_length=200)
    plot_type = models.ForeignKey(Plot_types, on_delete=models.DO_NOTHING)
    plot_category = models.ForeignKey(Plot_category, on_delete=models.DO_NOTHING)
    block = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now, blank=True)
    contact = models.CharField(max_length=200)
    remarks = models.CharField(max_length=2000)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    # def __str__(self):
    #     return self.title

    class Meta:
        verbose_name = "5. Plot Detail of Table Society"


class Society_details_home_page(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.CharField(max_length=1000)
    map = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.CharField(max_length=2000)
    details = models.CharField(max_length=2000)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "6. Society Detail Home Page"
