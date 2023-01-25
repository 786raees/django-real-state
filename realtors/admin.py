from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
  list_display = ('id','is_mvp', 'name','phone', 'email','photo','description','hire_date')
  list_display_links = ('id',)
  list_editable = ('is_mvp', 'name','phone', 'email', 'hire_date','photo','description')
  search_fields = ('name','email')
  list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)