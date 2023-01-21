from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('searchSociety/<int:id>', views.searchSociety, name='searchSociety'),
    path('society/<int:id>', views.society, name='society'),
    path('society-main/<int:id>', views.society_main_page, name='society-main'),
    path('society-phase/<int:id_society>/<int:id_phase>', views.society_phase_page, name='society-phase'),

]