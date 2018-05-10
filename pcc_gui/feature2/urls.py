from django.conf.urls import url

from . import views

app_name = 'feature2'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^loadfmm', views.loadfmm, name='loadfmm'),
    url(r'^group2', views.group_view2, name='group2'),
]
