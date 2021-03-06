# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.shortcuts import render

# from django.urls import reverse # future versions.
from django.core.urlresolvers import reverse_lazy


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def table(request):

    import pandas as pd
    import numpy as np

    df = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
    table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
    table = table.replace('border="1"','border="0"')
    table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.

    return HttpResponse(table)


from os.path import join
from django.conf import settings

def csv(request, year = None):

   import pandas as pd

   filename = join(settings.STATIC_ROOT, 'myapp/va_presidential.csv')

   df = pd.read_csv(filename)

   if year: df = df[df["Year"] == int(year)]

   table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
   table = table.replace('border="1"','border="0"')
   table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.

   return HttpResponse(table)


def greet(request, w):

    return HttpResponse("Well hello, {}!".format(w))


def add(request, p1, p2):

    p1 = int(p1)
    p2 = int(p2)

    return HttpResponse("{} + {} = {}".format(p1, p2, p1 + p2))


def greet_template(req, w):

  return render(req, "greet.html", {"who" : w})


def display_table(request):


   import pandas as pd

   filename = join(settings.STATIC_ROOT, 'myapp/va_presidential.csv')

   df = pd.read_csv(filename)

   table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
   table = table.replace('border="1"','border="0"')
   table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.


   return render(request, 'view_table.html', {"title" : "Virginia Presidential Elections",
                                              "html_table" : table})


def pure_template(req):

  params = {"xli" : ["Bessy", "has", "fantastic", "cats"],
            "animal" : "dog",
            "di" : {"dog" : "woof", "cat" : "meow", "tiger" : "roar"}}

  return render(req, "pure_template.html", params)


def get_reader(request): # note: no other params.

  state = request.GET.get('state', 'Fool!!')  # if we knew the parameters ...
  d = dict(request.GET._iterlists())
  return HttpResponse(str(state))


from .forms import InputForm
from .models import STATES_DICT

def form(request):

    state = request.GET.get('state', 'Fool')
    # if not state: state = request.POST.get('state', 'PA')

    params = {'form_action' : reverse_lazy('myapp:form'),
              'form_method' : 'get',
              'form' : InputForm({'state' : state}),
              'state' : STATES_DICT[state]}

    return render(request, 'form.html', params)


from django.views.generic import FormView
class FormClass(FormView):

    template_name = 'form.html'
    form_class = InputForm


    def get(self, request):

      state = request.GET.get('state', 'PA')

      return render(request, self.template_name, {'form_action' : reverse_lazy('myapp:formclass'),
                                                  'form_method' : 'get',
                                                  'form' : InputForm({'state' : state}),
                                                  'state' : STATES_DICT[state]})

    def post(self, request):

      state = request.POST.get('state', 'PA')

      return render(request, self.template_name, {'form_action' : reverse_lazy('myapp:formclass'),
                                                  'form_method' : 'get',
                                                  'form' : InputForm({'state' : state}),
                                                  'state' : STATES_DICT[state]})


import matplotlib.pyplot as plt, numpy as np

def pic(request, c = None):

   t = np.linspace(0, 2 * np.pi, 30)
   u = np.sin(t)

   plt.figure() # needed, to avoid adding curves in plot
   plt.plot(t, u, color = c)

   # write bytes instead of file.
   from io import BytesIO
   figfile = BytesIO()

   # this is where the color is used.
   try: plt.savefig(figfile, format = 'png')
   except ValueError: raise Http404("No such color")

   figfile.seek(0) # rewind to beginning of file
   return HttpResponse(figfile.read(), content_type="image/png")


def display_pic(request, c = 'r'):

    return render(request, 'view_pic.html', {"title" : "An astounding plot!",
                                             "pic_source" : reverse_lazy("myapp:pic_col", kwargs = {'c' : c})})


def resp_redirect(request):

    state = request.POST.get('state', '')
    if not state: state = request.GET.get('state', '')

    if state: return HttpResponseRedirect(reverse_lazy('myapp:resp', kwargs = {'state' : state}))

    return HttpResponseRedirect(reverse_lazy('myapp:form'))


def resp(request, state):

    return HttpResponse("I hear you, {}.".format(STATES_DICT[state]))


# homework-7 Laura Bergedieck
def county(request, county = None):

   import pandas as pd

   filename = join(settings.STATIC_ROOT, 'myapp/va_presidential.csv')

   df = pd.read_csv(filename)

   if county: df = df[df["County/City"].str.lower().str.contains(county.lower())]

   table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
   table = table.replace('border="1"','border="0"')
   table = table.replace('style="text-align: right;"', "")

   return HttpResponse(table)
