from django.contrib.sitemaps import Sitemap
from .models import Post, DevPost

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, item):
        return item.publish


# DevPost

class DevPostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return DevPost.published.all()

    def lastmod(self, item):
        return item.publish