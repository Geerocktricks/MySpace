from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .feeds import PostsFeed, DevPostsFeed
from .models import *


def add_post_ids_to_categories():
    for post in Post.objects.all():
        post.save()
add_post_ids_to_categories()


urlpatterns = [
    url(r'^$', views.post_list_view, name='post_list_view'),
    url(r'^programming/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.devpost_detail_view, name='devpost_detail_view'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail_view, name='post_detail_view'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^devsearch/', views.devsearch_results, name='devsearch_results'),
    url(r'^feed/$', PostsFeed(), name='post_feed'),
    url(r'^programmingfeed/$', DevPostsFeed(), name='devpost_feed'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.post_list_by_category, name='post_list_by_category'),
    url(r'^programming/(?P<kategory_slug>[-\w]+)/$', views.devpost_list_by_category, name='devpost_list_by_category'),
    url(r'^tag/(?P<kategory_slug>)/$', views.tagged, name='tagged'),
    url(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)