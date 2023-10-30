from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Quote,Category,Language,Author


class StaticViewSitemap(Sitemap):
    changefreq = 'Hourly'

    def items(self):
        return ['home', 'about', 'privacy-policy', 'terms-conditions']

    def location(self, item):
        return reverse(item)


class QuoteSitemap(Sitemap):
    changefreq = 'Hourly'
    priority = 0.8

    def items(self):
        return Quote.objects.all()

    def location(self, obj):
        return reverse('quotes', args=[obj.id])

class CategorySitemap(Sitemap):
    changefreq = 'Hourly'
    priority = 0.8

    def items(self):
        return Quote.objects.all()

    def location(self, obj):
        return reverse('quotes_by_categories', args=[obj.id,obj.name])


