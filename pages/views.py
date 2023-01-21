from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import *
from realtors.models import Realtor
from contacts.models import About, Team_members

def index(request):
    # Keywords
    keywords = request.GET.get('keywords')
    if keywords:
        city_data = city.objects.order_by('-list_date').filter(is_published=True).filter(title__icontains=keywords)
    else:
        city_data = city.objects.order_by('-list_date').filter(is_published=True)
    city_datas = city.objects.order_by('-list_date').filter(is_published=True)
    society_dropdown = Society.objects.order_by('-list_date').filter(is_published=True)
    contact_info = Owner_Contact_Us.objects.order_by('-list_date').filter(is_published=True)
    for i in contact_info.values():
        request.session['name'] =i['title']
        request.session['location'] = i['location']
        request.session['phone_number'] = i['phone_number']
        request.session['Mobile_number'] = i['Mobile_number']
        request.session['whatsapp_number'] = i['whatsapp_number']
        request.session['fb_id'] = i['fb_id']
        request.session['instagram_id'] = i['instagram_id']
        request.session['gmail_id'] = i['gmail_id']
        request.session['linkedin_id'] = i['linkedin_id']

    context = {
        'citys': city_data,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'city_dropdown':city_datas,
        'society_dropdowns':society_dropdown
    }

    return render(request, 'pages/index.html', context)


# def about(request):
#     # Get all realtors
#     realtors = Realtor.objects.order_by('-hire_date')
#     city_data = city.objects.order_by('-list_date').filter(is_published=True)
#     society_dropdown = Society.objects.order_by('-list_date').filter(is_published=True)
#
#     # Get MVP
#     mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
#
#     context = {
#         'realtors': realtors,
#         'mvp_realtors': mvp_realtors,
#         'city_dropdown':city_data,
#         'society_dropdowns': society_dropdown
#     }
#
#     return render(request, 'pages/about.html', context)


def about(request):
    # Get all realtors
    abouts = About.objects.order_by('-list_date').filter(is_published=True)
    city_data = city.objects.order_by('-list_date').filter(is_published=True)
    society_dropdown = Society.objects.order_by('-list_date').filter(is_published=True)
    team_members = Team_members.objects.order_by('-list_date').filter(is_published=True)
    # Get MVP
    mvp_team_member = Team_members.objects.all().filter(is_mvp_team_member=True)

    context = {
        'abouts':abouts,
        'team_members':team_members,
        'mvp_team_members':mvp_team_member,
        'city_dropdown':city_data,
        'society_dropdowns': society_dropdown
    }

    return render(request, 'pages/about.html', context)