from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.shortcuts import render

def website(req): return render(req, "website.html") # create a function that returns the website when called
