from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import *
from realtors.models import Realtor

def index(request):
    city_data = city.objects.order_by('-list_date').filter(is_published=True)
    city_datas = city.objects.order_by('-list_date').filter(is_published=True)
    society_dropdown = Society.objects.order_by('-list_date').filter(is_published=True)
    context = {
        'citys': city_data,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'city_dropdown':city_datas,
        'society_dropdowns':society_dropdown
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    city_data = city.objects.order_by('-list_date').filter(is_published=True)
    society_dropdown = Society.objects.order_by('-list_date').filter(is_published=True)

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
        'city_dropdown':city_data,
        'society_dropdowns': society_dropdown
    }

    return render(request, 'pages/about.html', context)


def searchCity(request):
    city_data = city.objects.order_by('-list_date').filter(is_published=True)
    society_dropdown = Society.objects.order_by('-list_date').filter(is_published=True)
    queryset_list  = city.objects.order_by('-list_date').filter(is_published=True)

  # Keywords
    keywords = request.GET.get('keywords')
    if keywords:
        queryset_list = queryset_list.filter(title__icontains=keywords)

    context = {
    'citys': queryset_list,
    'values': request.GET,
      'city_dropdown':city_data,
        'society_dropdowns': society_dropdown
    }

    return render(request, 'pages/index.html', context)