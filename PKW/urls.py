from django.conf.urls import url

from . import views

app_name = 'PKW'

urlpatterns = [
    url(r'^editing/inh', views.editing_byinh),
    url(r'^editing/voiv', views.editing_byvoiv),
    url(r'^editing/type', views.editing_bytype),
    url(r'^editing/save', views.editing_save),
    url(r'^login/$', views.loginView),

    url(r'^rest/districts/$', views.listDistricts),
    url(r'^rest/voivodeships/$', views.listVoivodeships),
    url(r'^rest/candidates/$', views.listCandidates),
]