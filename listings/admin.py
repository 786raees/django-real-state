from django.contrib import admin

from .models import *

class PlotTypesAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'title')
  list_display_links = ('id', )
  list_filter = ('title',)
  list_editable = ('is_published','title')
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Plot_types, PlotTypesAdmin)

class SocietyLatestNewAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'title')
  list_display_links = ('id', )
  list_filter = ('title',)
  list_editable = ('is_published','title')
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Socity_latest_news, SocietyLatestNewAdmin)

class SocityStatusAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'title')
  list_display_links = ('id', )
  list_filter = ('title',)
  list_editable = ('is_published','title')
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Socity_Status, SocityStatusAdmin)
class PlotCategoryAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'title')
  list_display_links = ('id',)
  list_filter = ('title',)
  list_editable = ('is_published','title')
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Plot_category, PlotCategoryAdmin)


class SocityPhaseAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'title')
  list_display_links = ('id',)
  list_filter = ('title',)
  list_editable = ('is_published','title')
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Socity_phase, SocityPhaseAdmin)

class SocietyAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'title','address','photo_main', 'city', 'state', 'zipcode',)
  list_display_links = ('id',)
  list_filter = ('realtor',)
  list_editable = ('is_published','title','photo_main','address','city', 'state',)
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Society, SocietyAdmin)

class SocityYoutubeAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'society','yut_video_1','yut_video_2','yut_video_3','yut_video_4','yut_video_5','yut_video_6',)
  list_display_links = ('id',)
  list_filter = ('title',)
  list_editable = ('is_published','society','yut_video_1','yut_video_2','yut_video_3','yut_video_4','yut_video_5','yut_video_6',)
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Society_Youtube_videos, SocityYoutubeAdmin)

class SocityHomePageImageAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'society','title','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6','photo_7','photo_8','photo_9','photo_10')
  list_display_links = ('id',)
  list_filter = ('title',)
  list_editable = ('is_published','society','title','photo_main','photo_1','photo_2','photo_3','photo_5','photo_6','photo_7','photo_8','photo_9','photo_10')
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Society_Home_Page_Images, SocityHomePageImageAdmin)
class SocityContactUsAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'society','location','phone_number','Mobile_number','whatsapp_number','fb_id','instagram_id','gmail_id','linkedin_id')
  list_display_links = ('id',)
  list_filter = ('society','location')
  list_editable = ('is_published','society','location','phone_number','Mobile_number','whatsapp_number','fb_id','instagram_id','gmail_id','linkedin_id')
  search_fields = ('society','location')
  list_per_page = 25

admin.site.register(Society_Contact_Us, SocityContactUsAdmin)
class ListingAdmin(admin.ModelAdmin):
  list_display = ('id','society', 'title', 'is_published', 'price','video_url','address','description','bedrooms','bathrooms',
                  'garage','square_foot','plot_size','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6')
  list_display_links = ('id', )
  list_filter = ('society',)
  list_editable = ('is_published','society','title','price','video_url','address','description','bedrooms','bathrooms',
                  'garage','square_foot','plot_size','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6')
  search_fields = ('title', 'description', 'address', 'price')
  list_per_page = 25

admin.site.register(Listing, ListingAdmin)


class PlotDetailsTableAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'society', 'society_phase', 'dimension','plot_type','plot_category',
                  'block', 'price', 'contact', 'remarks', 'is_published')
  list_display_links = ('id',)
  list_filter = ('society','society_phase')
  list_editable = ('is_published', 'society', 'society_phase', 'dimension','plot_type','plot_category',
                  'block', 'price', 'contact', 'remarks', 'is_published')
  search_fields = ('society','society_phase')
  list_per_page = 25

admin.site.register(Plot_details_table, PlotDetailsTableAdmin)


class SocietyDetailsHomePageAdmin(admin.ModelAdmin):
  list_display = ('id', 'society', 'is_published', 'plot_types', 'society_status', 'rating','launch_date','approvals',
                  'facilities','transfer_charges','transfer_office','location_on_map','society_location',
                  'official_website','official_contact_number','posession','posession_date','description_and_details_1',
                  'description_and_details_1')
  list_display_links = ('id',)
  list_filter = ('society',)
  list_editable = ('society', 'is_published', 'plot_types', 'society_status', 'rating','launch_date','approvals',
                  'facilities','transfer_charges','transfer_office','location_on_map','society_location',
                  'official_website','official_contact_number','posession','posession_date','description_and_details_1',
                   'description_and_details_1')
  search_fields = ('society', 'description',)
  list_per_page = 25

admin.site.register(Society_details_home_page, SocietyDetailsHomePageAdmin)