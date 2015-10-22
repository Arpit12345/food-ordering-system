from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import placeorder
from django.views import generic

def index(request):
    response = "Hello, Welcome to Food Ordering System!"
    template = loader.get_template('orderplace/place_order.html')
    context = RequestContext(request, {'response': response})

    return HttpResponse(template.render(context))




def form(request):
    response1 = "Place your order"
    template1 = loader.get_template('orderplace/form.html')
    context = RequestContext(request, {'response': response1})
    return HttpResponse(template1.render(context))





