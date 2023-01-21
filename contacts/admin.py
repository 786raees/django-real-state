from django.contrib import admin

from .models import Contact, Team_members, About

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'listing', 'email', 'contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', 'listing')
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)


class TeamAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'photo_main','is_mvp_team_member','description')
  list_display_links = ('id', )
  list_editable =('name', 'photo_main','is_mvp_team_member','description')
  search_fields = ('name','is_mvp_team_member')
  list_per_page = 25

admin.site.register(Team_members, TeamAdmin)


class AboutAdmin(admin.ModelAdmin):
  list_display = ('id','is_published', 'description','title','we_work_message','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6','photo_7','photo_8','photo_9','photo_10')
  list_display_links = ('id', )
  list_editable = ('is_published','description','title','we_work_message','photo_main','photo_1','photo_2','photo_3','photo_5','photo_6','photo_7','photo_8','photo_9','photo_10')
  search_fields = ('title', 'description')
  list_per_page = 25

admin.site.register(About, AboutAdmin)