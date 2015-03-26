# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, RequestContext

def home (request):
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))


# Create your views here.
