from django.conf.urls import url

from . import views

from . import w6

app_name = 'myapp'
urlpatterns = [

    # November 7
    url(r'^$', views.index, name='index'),
    url(r'^table/$', views.table),
    url(r'^csv/$', views.csv),
    url(r'^csv/(?P<year>[0-9]+)/$', views.csv),
    url(r'^greet/(?P<w>[A-Za-z\- ]+)/$', views.greet),
    url(r'^add/(?P<p1>[0-9]+)\+(?P<p2>[0-9]+)/$', views.add, name='add'),
    url(r'^greet_template/(?P<w>[A-Za-z\- ]+)/$', views.greet_template),

    # November 9
    url(r'^pure_template/$', views.pure_template),

    url(r'^get_reader/$', views.get_reader, name='get_reader'),
    url(r'^form/$', views.form, name = "form"),
    url(r'^pic/$', views.pic, name='pic'),
    url(r'^pic/(?P<c>[a-z])/$', views.pic, name='pic_col'),
    url(r'^display_pic/$', views.display_pic, name='display_pic'),
    url(r'^display_pic/(?P<c>[a-z])/$', views.display_pic, name='display_pic_col'),
    url(r'^display_table/$', views.display_table, name='display_table'),
    url(r'^formclass/$', views.FormClass.as_view(), name = "formclass"),
    # url(r'^resp/$', views.resp_redirect, name = "resp_redirect"),
    # url(r'^resp/(?P<state>[A-Z][A-Z])/$', views.resp, name = "resp"),

    # hw-7-LauraBer: link to my website in the view called w6
    url(r'^website/$', w6.website, name='website'),
    url(r'^county/(?P<county>[A-Za-z\- ]+)/$', views.county),
]
