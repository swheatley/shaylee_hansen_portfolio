from django.shortcuts import render, render_to_response
from django.conf import settings 
from django.template import RequestContext


def index(request):
    context = {}
    return render_to_response('index.html', context, context_instance=RequestContext(request))


def index2(request):
    context = {}
    return render_to_response('index2.html', context, context_instance=RequestContext(request))


def about_me(request):
    context = {}
    return render_to_response('about-me-index.html', context, context_instance=RequestContext(request))

# Projects


def projects(request):
    context = {}
    return render_to_response('Projects/projects.html', context, context_instance=RequestContext(request))


def google(request):
    context = {}
    return render_to_response('Projects/google.html', context, context_instance=RequestContext(request))


def google_search(request):
    context = {}
    return render_to_response('Projects/google_search.html', context, context_instance=RequestContext(request)) 


def luigi_bootstrap(request):
    context = {}
    return render_to_response('Projects/luigi.html', context, context_instance=RequestContext(request))


def color_grid(request):
    context = {}
    return render_to_response('Projects/grid.html', context, context_instance=RequestContext(request))


def jquery_fighter(request):
    context = {}
    return render_to_response('Projects/j_streetfighter.html', context, context_instance=RequestContext(request))


def landing_page(request):
    context = {}
    return render_to_response('Projects/landing_page.html', context, context_instance=RequestContext(request))
