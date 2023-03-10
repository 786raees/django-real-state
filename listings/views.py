from datetime import datetime

from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
from django.shortcuts import redirect
from django.contrib import messages
from .models import *

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)
  city_data = city.objects.order_by('-list_date').filter(is_published=True)
  society_dropdown = Society.objects.order_by('-list_date').filter(is_published=True)

  context = {
    'city_dropdown': city_data,
    'society_dropdowns': society_dropdown,
    'listings': paged_listings,
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices
  }

  return render(request, 'listings/listings.html', context)

def society(request, id):
  city_data = city.objects.order_by('-list_date').filter(is_published=True)
  city_id=city.objects.filter(id=id).first()
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    society = Society.objects.order_by('-list_date').filter(is_published=True).filter(city=city_id).filter(
      title__icontains=keywords)
  else:
    society = Society.objects.order_by('-list_date').filter(is_published=True).filter(city=city_id)
  society_dropdown = Society.objects.order_by('-list_date').filter(is_published=True)

  context = {
      'societys': society,
      'state_choices': state_choices,
      'city_id':city_id.id,
      'city_dropdown':city_data,
    'society_dropdowns': society_dropdown
    }
  return render(request, 'pages/societys.html', context)
def society_main_page(request, id):
  city_data = city.objects.order_by('-list_date').filter(is_published=True)
  society_id = Society.objects.filter(id=id).first()
  society_desc = Society.objects.filter(id=id)
  # society_transfer_office= Socity_transfer_office.objects.order_by('-list_date').filter(is_published=True).filter(society=society_id)
  # society_main = Society_details_home_page.objects.order_by('-list_date').filter(is_published=True).filter(society=society_id)
  # society_plot_table_data = Plot_details_table.objects.order_by('-list_date').filter(is_published=True).filter(society=society_id)
  # latest_news = Socity_latest_news.objects.order_by('-list_date').filter(is_published=True).filter(society=society_id)
  society_phases = Society_phase_details_home_page.objects.order_by('-list_date').filter(is_published=True).filter(society=society_id)
  society_tags = Socity_tags.objects.order_by('-list_date').filter(is_published=True).filter(society=society_id)
  society_dropdown = Society.objects.order_by('-list_date').filter(is_published=True)
  # society_rating = Socity_Rating.objects.order_by('-list_date').filter(is_published=True).filter(society=society_id)
  # total_rating = len(society_rating)
  # total_rate = 0
  # try:
  #   for rate in society_rating:
  #     total_rate = total_rate + rate.rate
  #   total_society_rating = total_rate/total_rating
  # except:
  #   total_society_rating = 0

  context = {
    # 'society_transfer_offices':society_transfer_office,
    # 'total_society_rating':total_society_rating,
    # 'society_ratings':society_rating,
    'city_dropdown':city_data,
    #   'society_mains': society_main,
      'state_choices': state_choices,
    'society_desc': society_desc,
      'society_id': society_id.id,
      # 'society_plot_table_datas':society_plot_table_data,
    # 'latest_news':latest_news,
    'society_phases':society_phases,
    'society_tags':society_tags,
    'society_dropdowns': society_dropdown
    }
  return render(request, 'listings/society_main_page.html', context)

def society_phase_page(request, id_society,id_phase):
  dates = request.GET.get('date')

  city_data = city.objects.order_by('-list_date').filter(is_published=True)
  society_id = Society.objects.filter(id=id_society).first()
  phase_id = Socity_phase.objects.filter(id=id_phase).first()
  society_transfer_office= Socity_transfer_office.objects.order_by('-list_date').filter(is_published=True).filter(society_phase=phase_id)
  phase_main = Society_phase_details_home_page.objects.order_by('-list_date').filter(is_published=True)\
    .filter(society=society_id).filter(society_phase=phase_id)
  if dates:
    phase_plot_table_data = Plot_phase_details_table.objects.order_by('-list_date').filter(is_published=True,
                                                                                           society=society_id,
                                                                                           society_phase=phase_id,
                                                                                           created_at__date=datetime.strptime(dates, '%Y-%m-%d'))
  else:
    phase_plot_table_data = Plot_phase_details_table.objects.order_by('-list_date').filter(is_published=True) \
      .filter(society=society_id).filter(society_phase=phase_id)
  latest_news = Socity_latest_news.objects.order_by('-list_date').filter(is_published=True).filter(society_phase=phase_id)
  society_dropdown = Society.objects.order_by('-list_date').filter(is_published=True)
  phase_rating = Socity_Rating.objects.order_by('-list_date').filter(is_published=True).filter(society=society_id).filter(society_phase=phase_id)
  socity_phase_maps = Socity_phase_maps.objects.order_by('-list_date').filter(is_published=True).filter(society=society_id).filter(society_phase=phase_id)
  socity_phase_other_documents = Socity_phase_other_documents_download.objects.order_by('-list_date').filter(is_published=True).filter(society=society_id).filter(society_phase=phase_id)
  socity_phase_approved_froms = Socity_phase_approved_from.objects.order_by('-list_date').filter(is_published=True).filter(society=society_id).filter(society_phase=phase_id)

  total_rating = len(phase_rating)
  total_rate = 0
  try:
    for rate in phase_rating:
      total_rate = total_rate + rate.rate
    total_phase_rating = total_rate/total_rating
  except:
    total_phase_rating = 0
  context = {
    'society_transfer_offices': society_transfer_office,
    'total_phase_rating': total_phase_rating,
    'phase_ratings': phase_rating,
    'city_dropdown':city_data,
      'phase_mains': phase_main,
      'state_choices': state_choices,
      'society_id': society_id.id, # type: ignore
      'phase_plot_table_datas':phase_plot_table_data,
    'latest_news':latest_news,
    'society_dropdowns':society_dropdown,
    'socity_phase_maps':socity_phase_maps,
    'socity_phase_other_documents':socity_phase_other_documents,
    'socity_phase_approved_froms':socity_phase_approved_froms,
    'phase_id':phase_id.id,
    }
  return render(request, 'listings/phase_main_page.html', context)
def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
  city_data = city.objects.order_by('-list_date').filter(is_published=True)
  society_dropdown = Society.objects.order_by('-list_date').filter(is_published=True)
  context = {
    'city_dropdown': city_data,
    'society_dropdowns': society_dropdown,
    'listing': listing
  }

  return render(request, 'listings/listing.html', context)

def search(request):
  queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)
  city_data = city.objects.order_by('-list_date').filter(is_published=True)
  society_dropdown = Society.objects.order_by('-list_date').filter(is_published=True)
  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(title__icontains=keywords)

  # City
  if 'city' in request.GET:
    city1 = request.GET.get('city')
    if city1:
      queryset_list = queryset_list.filter(socity_phase_sector__society__city__title__contains=city1)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(socity_phase_sector__society__state__contains=state)

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
    'city_dropdown': city_data,
    'society_dropdowns': society_dropdown,
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context)


def rating(request):
  if request.method == 'POST':
    rate = request.POST['rate']
    message = request.POST['message']
    society_id_1 = request.POST['society_id']
    phase_id_1 = request.POST['phase_id']
    user_id = request.POST['user_id']
    society_id = Society.objects.filter(id=society_id_1).first()
    phase_id = Socity_phase.objects.filter(id=phase_id_1).first()
    user_id = User.objects.filter(id=user_id).first()
    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      # user_id = request.user.id
      has_contacted = Socity_Rating.objects.all().filter(society=society_id, society_phase=phase_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an Review against this Society Phase !')
        return redirect(f'/listings/society-phase/{society_id_1}/{phase_id_1}')

    contact = Socity_Rating(society=society_id, society_phase=phase_id, user_id=user_id, comment=message,rate=rate )

    contact.save()
    messages.success(request, 'Your request has been submitted,Thanks')
    return redirect(f'/listings/society-phase/{society_id_1}/{phase_id_1}')
