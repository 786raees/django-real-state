from django.contrib import admin
from django.utils.html import format_html
from .models import *

class SocityTransferOfficeAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'society','society_phase','office_name','office_contact_no','office_address','office_google_map','description_and_details')
  list_display_links = ('id', )
  list_filter = ('society',)
  list_editable = ('is_published','society','society_phase','office_name','office_contact_no','office_address','office_google_map','description_and_details')
  search_fields = ('society','society_phase',)
  list_per_page = 25

admin.site.register(Socity_transfer_office, SocityTransferOfficeAdmin)


class PlotTypesAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'title')
  list_display_links = ('id', )
  list_filter = ('title',)
  list_editable = ('is_published','title')
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Plot_types, PlotTypesAdmin)

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


class SocitySectorAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'title')
  list_display_links = ('id',)
  list_filter = ('title',)
  list_editable = ('is_published','title')
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Socity_Sector, SocitySectorAdmin)

class SocityTagsAdmin(admin.ModelAdmin):
  list_display = ('id','is_published','society', 'title')
  list_display_links = ('id',)
  list_filter = ('title',)
  list_editable = ('is_published','society','title')
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Socity_tags, SocityTagsAdmin)

class SocityLatestNewsAdmin(admin.ModelAdmin):
  list_display = ('id','is_published','society','news_link','society_phase', 'title')
  list_display_links = ('id',)
  list_filter = ('title',)
  list_editable = ('is_published','society','news_link','society_phase','title')
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Socity_latest_news, SocityLatestNewsAdmin)

class CityAdmin(admin.ModelAdmin):
  def image_tag(self, obj):
    return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.photo_main.url))

  list_display = ('id','is_published', 'title','image_tag','photo_main')
  list_display_links = ('id',)
  list_filter = ('title',)
  list_editable = ('is_published','title','photo_main')
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(city, CityAdmin)


class SocityRatingAdmin(admin.ModelAdmin):
  list_display = ('id','is_published','society','society_phase','comment','rate')
  list_display_links = ('id',)
  list_filter = ('rate',)
  list_editable = ('is_published','society','society_phase','comment','rate')
  search_fields = ('rate','comment')
  list_per_page = 25


admin.site.register(Socity_Rating, SocityRatingAdmin)

class SocietyAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'title','address','photo_main', 'city', 'state', 'zipcode',)
  list_display_links = ('id',)
  list_filter = ('title',)
  list_editable = ('is_published','title','photo_main','address','city', 'state',)
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Society, SocietyAdmin)


class SocietyPhaseSectorAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'society','society_phase','society_sector',)
  list_display_links = ('id',)
  list_filter = ('society_sector',)
  list_editable = ('is_published','society','society_phase','society_sector')
  search_fields = ('society_sector',)
  list_per_page = 25

admin.site.register(Socity_phase_Sector, SocietyPhaseSectorAdmin)
class SocityYoutubeAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'society','yut_video_1','yut_video_2','yut_video_3','yut_video_4','yut_video_5','yut_video_6',)
  list_display_links = ('id',)
  list_filter = ('title',)
  list_editable = ('is_published','society','yut_video_1','yut_video_2','yut_video_3','yut_video_4','yut_video_5','yut_video_6',)
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Society_Youtube_videos, SocityYoutubeAdmin)

class SocityPhaseYoutubeAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'society','society_phase','yut_video_1','yut_video_2','yut_video_3','yut_video_4','yut_video_5','yut_video_6',)
  list_display_links = ('id',)
  list_filter = ('title',)
  list_editable = ('is_published','society','yut_video_1','yut_video_2','yut_video_3','yut_video_4','yut_video_5','yut_video_6',)
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Society_Phase_Youtube_videos, SocityPhaseYoutubeAdmin)

class SocityHomePageImageAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'society','title','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6','photo_7','photo_8','photo_9','photo_10')
  list_display_links = ('id',)
  list_filter = ('title',)
  list_editable = ('is_published','society','title','photo_main','photo_1','photo_2','photo_3','photo_5','photo_6','photo_7','photo_8','photo_9','photo_10')
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Society_Home_Page_Images, SocityHomePageImageAdmin)


class SocityPhaseHomePageImageAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'society','society_phase','title','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6','photo_7','photo_8','photo_9','photo_10')
  list_display_links = ('id',)
  list_filter = ('title',)
  list_editable = ('is_published','society','title','photo_main','photo_1','photo_2','photo_3','photo_5','photo_6','photo_7','photo_8','photo_9','photo_10')
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Society_Phase_Home_Page_Images, SocityPhaseHomePageImageAdmin)
class OwnerContactUsAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'title','location','phone_number','Mobile_number','whatsapp_number','fb_id','instagram_id','gmail_id','linkedin_id')
  list_display_links = ('id',)
  list_filter = ('location',)
  list_editable = ('is_published','title','location','phone_number','Mobile_number','whatsapp_number','fb_id','instagram_id','gmail_id','linkedin_id')
  search_fields = ('location',)
  list_per_page = 25

admin.site.register(Owner_Contact_Us, OwnerContactUsAdmin)
class ListingAdmin(admin.ModelAdmin):
  list_display = ('id','socity_phase_sector','block','plot_no', 'title', 'is_published', 'price','video_url','address','description','bedrooms','bathrooms',
                  'garage','square_foot','plot_size','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6')
  list_display_links = ('id', )
  list_filter = ('socity_phase_sector',)
  list_editable = ('is_published','socity_phase_sector','block','plot_no','title','price','video_url','address','description','bedrooms','bathrooms',
                  'garage','square_foot','plot_size','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6')
  search_fields = ('title', 'description', 'address', 'price')
  list_per_page = 25

admin.site.register(Listing, ListingAdmin)


class PlotDetailsTableAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'society', 'dimension','plot_type','society_phase','plot_category',
                  'block', 'price', 'contact', 'remarks',)
  list_display_links = ('id',)
  list_filter = ('society',)
  list_editable = ('is_published', 'society', 'dimension','plot_type','plot_category',
                  'block', 'price', 'contact','society_phase', 'remarks',)
  search_fields = ('society',)
  list_per_page = 25

admin.site.register(Plot_details_table, PlotDetailsTableAdmin)


class PlotPhaseDetailsTableAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'society', 'society_phase', 'dimension','plot_type','plot_category',
                  'block', 'price', 'contact', 'remarks')
  list_display_links = ('id',)
  list_filter = ('society','society_phase')
  list_editable = ('is_published', 'society', 'society_phase', 'dimension','plot_type','plot_category',
                  'block', 'price', 'contact', 'remarks')
  search_fields = ('society','society_phase')
  list_per_page = 25

admin.site.register(Plot_phase_details_table, PlotPhaseDetailsTableAdmin)

class SocietyDetailsHomePageAdmin(admin.ModelAdmin):
  list_display = ('id','title', 'society', 'is_published', 'plot_types', 'society_status','launch_date','approvals','download_location_file',
                  'facilities','transfer_charges','transfer_office','location_on_map','society_location',
                  'official_website','official_contact_number','posession','posession_date','description_and_details_1',
                  'description_and_details_2')
  list_display_links = ('id',)
  list_filter = ('society',)
  list_editable = ('title','society', 'is_published', 'plot_types', 'society_status','launch_date','approvals','download_location_file',
                  'facilities','transfer_charges','transfer_office','location_on_map','society_location',
                  'official_website','official_contact_number','posession','posession_date','description_and_details_1',
                   'description_and_details_2')
  search_fields = ('society', 'description',)
  list_per_page = 25

admin.site.register(Society_details_home_page, SocietyDetailsHomePageAdmin)




class SocietyPhaseDetailsHomePageAdmin(admin.ModelAdmin):
  list_display = ('id','title', 'society', 'is_published', 'plot_types','society_phase', 'society_status','launch_date','approvals','download_location_file',
                  'gas_facilities','water_facilities','mantaince_facilities','secuirty_facilities','sav_facilities','electricity_facilities','transfer_charges','transfer_office','location_on_map','society_location',
                  'official_website','official_contact_number','posession','posession_date','description_and_details_1',
                  'description_and_details_2')
  list_display_links = ('id',)
  list_filter = ('society',)
  list_editable = ('title','society', 'is_published', 'plot_types','society_phase', 'society_status','launch_date','approvals','download_location_file',
                  'gas_facilities','water_facilities','mantaince_facilities','secuirty_facilities','sav_facilities','electricity_facilities',
                   'transfer_charges','transfer_office','location_on_map','society_location',
                  'official_website','official_contact_number','posession','posession_date','description_and_details_1',
                   'description_and_details_2')
  search_fields = ('society', 'description',)
  list_per_page = 25

admin.site.register(Society_phase_details_home_page, SocietyPhaseDetailsHomePageAdmin)