from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices

from .models import *

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings,
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices
  }

  return render(request, 'listings/listings.html', context)

def society(request, id):
  city_id=city.objects.filter(id=id).first()
  society = Society.objects.order_by('-list_date').filter(is_published=True).filter(city=city_id)

  context = {
      'societys': society,
      'state_choices': state_choices,
      'city_id':city_id.id
    }
  return render(request, 'pages/societys.html', context)
def society_main_page(request, id):
  society_id = Society.objects.filter(id=id).first()
  society_main = Society_details_home_page.objects.order_by('-list_date').filter(is_published=True).filter(society=society_id)
  society_plot_table_data = Plot_details_table.objects.order_by('-list_date').filter(is_published=True).filter(society=society_id)
  context = {
      'society_mains': society_main,
      'state_choices': state_choices,
      'society_id': society_id.id,
      'society_plot_table_datas':society_plot_table_data
    }
  return render(request, 'listings/society_main_page.html', context)
def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
    'listing': listing
  }

  return render(request, 'listings/listing.html', context)

def search(request):
  queryset_list = Listing.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context)


def searchSociety(request, id):
  city_id = city.objects.filter(id=id).first()
  queryset_list  = Society.objects.order_by('-list_date').filter(is_published=True).filter(city=city_id)

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(address__icontains=keywords)

  # # City
  # if 'city' in request.GET:
  #   city = request.GET['city']
  #   if city:
  #     queryset_list = queryset_list.filter(city__iexact=city)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)


  context = {
    'state_choices': state_choices,
    'societys': queryset_list,
    'values': request.GET
  }

  return render(request, 'pages/societys.html', context)


