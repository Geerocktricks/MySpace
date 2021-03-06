from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post, DevPost

class PostsFeed(Feed):
    title = 'Diaries of a KenyanDreamer'
    link = '/blog/'
    description = 'Our latest Posts!'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 20)

class DevPostsFeed(Feed):
    title = 'Diaries of a KenyanDreamer'
    link = '/blog/'
    description = 'Our latest Programming tutorials!'

    def items(self):
        return DevPost.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 20)