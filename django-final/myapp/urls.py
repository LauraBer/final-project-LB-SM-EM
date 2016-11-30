from django.conf.urls import url



from . import projectview

app_name = 'myapp'
urlpatterns = [

    # try if website works at all
    url(r'^$', projectview.test, name='index'),

    # link to our website for the final project
    url(r'^website/$', projectview.website, name='website'),

    ]
