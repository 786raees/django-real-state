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
  list_display = ('id','is_published', 'title','address', 'city', 'state', 'zipcode',)
  list_display_links = ('id',)
  list_filter = ('realtor',)
  list_editable = ('is_published','title')
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(Society, SocietyAdmin)

class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'society')
  list_display_links = ('id', 'title')
  list_filter = ('society',)
  list_editable = ('is_published',)
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
  list_per_page = 25

admin.site.register(Listing, ListingAdmin)


class PlotDetailsTableAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'society', 'society_phase', 'dimension','plot_type','plot_category',
                  'block', 'price', 'date', 'contact', 'remarks', 'is_published')
  list_display_links = ('id',)
  list_filter = ('society','society_phase')
  list_editable = ('is_published', 'society', 'society_phase', 'dimension','plot_type','plot_category',
                  'block', 'price', 'date', 'contact', 'remarks', 'is_published')
  search_fields = ('society','society_phase')
  list_per_page = 25

admin.site.register(Plot_details_table, PlotDetailsTableAdmin)


class SocietyDetailsHomePageAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'video_url', 'list_date', 'details','description')
  list_display_links = ('id',)
  list_filter = ('title',)
  list_editable = ('title', 'is_published', 'video_url', 'list_date', 'details','description')
  search_fields = ('title', 'description',)
  list_per_page = 25

admin.site.register(Society_details_home_page, SocietyDetailsHomePageAdmin)