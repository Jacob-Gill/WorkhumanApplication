from django.shortcuts import render
from .models import Country

def country_list(request):
    query = request.GET.get('q', '')  # Search query
    continent_filter = request.GET.get('continent', '')  # Continent filter

    # Query all countries
    countries = Country.objects.all()

    # Apply search and filter
    if query:
        countries = countries.filter(name__icontains=query)
    if continent_filter and continent_filter != 'all':
        countries = countries.filter(continent=continent_filter)

    # Get unique continents for the dropdown
    all_continents = Country.objects.values_list('continent', flat=True).distinct()

    return render(request, 'countryapp/country_list.html', {
        'countries': countries,
        'query': query,
        'continent_filter': continent_filter,
        'all_continents': sorted(all_continents),
    })
