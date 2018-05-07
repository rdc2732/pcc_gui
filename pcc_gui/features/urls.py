from django.conf.urls import url

from . import views

app_name = 'features'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^loadfmm', views.loadfmm, name='loadfmm'),
    url(r'^features', views.FeatureListView.as_view(), name='features'),
    url(r'^groups', views.group_view, name='groups'),
]
