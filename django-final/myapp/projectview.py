from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.shortcuts import render

from django.core.urlresolvers import reverse_lazy

def test(request):
    return HttpResponse("Hello, Shaun, Enrique and Laura. You're are a great team and we will try the website next.")

def website(req): # return render(req, "website.html") # create a function that returns the website when called
    import pandas as pd

    # for dropdown *not sure if this works
    from .forms import InputForm
    from .models import LGAs_DICT

    lga = req.GET.get('lga', 'Banana')

    # include the table on housing
    from os.path import join
    from django.conf import settings

    filename = join(settings.STATIC_ROOT, 'myapp/housing.csv')
    #  this was in the website.html that did not work: <img src='static/myapp/map.png' alt="Queensland" width=32 height=32>
    housing = pd.read_csv(filename, index_col=0)
    filteredseries = housing.loc[lga]
    housingfiltered = filteredseries.to_frame() # create a table that only shows the row for the lga selected


    # create a new data frame that includes only the row for Banana (as an example), check how Jamie did it in class for his examples in jupyter
    table = housingfiltered.to_html()#float_format = "%.3f", classes = "table table-striped", index_names = False)
    #table = table.replace('border="1"','border="0"')
    #table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.

    params = {'form_action' : reverse_lazy('myapp:website'),
              'form_method' : 'get',
              'form' : InputForm({'lga' : lga}),
              'lga' : LGAs_DICT[lga],
              "html_table" : table}
    return render(req, 'website.html', params)
