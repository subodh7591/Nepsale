from django.conf.urls import url
from . import views

app_name='category'

urlpatterns = [
    url(r'^$',views.index1, name='index1'),

    #/tac/712/
    url(r'^(?P<item_id>[0-9]+)$',views.detail,name='detail'),
]