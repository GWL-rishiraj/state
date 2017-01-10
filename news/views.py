from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import View

def common_template_variables(request):
    """
    This is used for template variables that will be used in all views, even
    across other views files.
    """
    tvars = {}
    return tvars

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    template_variables = common_template_variables(request)
    template_variables['title'] = "Home Page"
    template_variables['content'] = "This is home page content"

    return render_to_response(
        'home.html',
        template_variables,
        context_instance=RequestContext(request)
    )

def register(request):
    return HttpResponse("register page")
