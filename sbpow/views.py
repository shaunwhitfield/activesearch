from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q

from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse

from .models import PlaceOfWorship

def build_filter(search_term):
    filter_list = []
    for field_name in [f.name for f in PlaceOfWorship._meta.get_fields()]:
        # ie. "Q(city__icontains='South')"
        filter_list.append(Q(**{f"{field_name}__icontains": search_term}))

    # pop the first item off and OR/Equal the rest
    filter = filter_list.pop()
    for filter_item in filter_list:
        filter |= filter_item
    return filter

def htmx_search_view(request):
    if request.method == "POST":
        search_term = request.POST.get('search', None)
        items = PlaceOfWorship.objects.filter(build_filter(search_term)).order_by('name')
        template = 'htmx/search_results.html'
    else:
        items = PlaceOfWorship.objects.all().order_by('name')
        template = 'htmx/search.html'
    return render(request=request, template_name=template, context={'items': items,})

@csrf_exempt
def ajax_search_view(request):
    if request.method == 'POST':
        search_term = request.POST.get('search_term', None)
        items = PlaceOfWorship.objects.filter(build_filter(search_term)).order_by('name')
        data = serializers.serialize('json', items)
        return JsonResponse({'data': data}, safe=False)
    else:
        items = PlaceOfWorship.objects.all().order_by('name')
        return render(request, 'ajax/search.html', {'items': items})