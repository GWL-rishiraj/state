from django.shortcuts import render , render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.generic.base import View
from models import *
# Create your views here.

def all_items(request):
    temp_var = {}
    temp_var['title'] = 'All Items'
    temp_var['items'] = Items.objects.all()
    return render_to_response(
        'items/items.html',
        temp_var,
        context_instance = RequestContext(request)
    )
    #return HttpResponse('all items')

def item(request,sku):
    temp_var = {}
    temp_var['title'] = 'Single Items'
    temp_var['item'] = Items.objects.get(sku=sku)
    return render_to_response(
        'items/item.html',
        temp_var,
        context_instance = RequestContext(request)
    )




