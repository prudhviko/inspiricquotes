from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from django.urls import reverse
from .models import Quote,Category,Language,Author
from django.utils.text import slugify


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
        return Category.objects.all()

    def location(self, obj):
        return reverse('quotes_by_categories', args=[obj.id,slugify(obj.name)])

class DisplayQuotesCategorySitemap(Sitemap):
    changefreq = 'Hourly'
    priority = 0.8

    def items(self):
        return Quote.objects.all()
    
    def location(self, obj):
        return reverse('display_quotes_categories', args=[obj.id,obj.category.id])


class LanguageSitemap(Sitemap):
    changefreq = 'Hourly'
    priority = 0.8

    def items(self):
        return Language.objects.all()
    
    def location(self, obj):
        return reverse('quotes_by_languages', args=[obj.id,slugify(obj.name)])

class DisplayQuotesLanguageSitemap(Sitemap):
    changefreq = 'Hourly'
    priority = 0.8

    def items(self):
        return Quote.objects.all()
    
    def location(self, obj):
        return reverse('display_quotes_languages', args=[obj.id,obj.language.id])

class AuthorSitemap(Sitemap):
    changefreq = 'Hourly'
    priority = 0.8

    def items(self):
        return Author.objects.all()
    
    def location(self,obj):
        return reverse('quotes_by_authors',args=[obj.id,slugify(obj.name)])

class DisplayQuotesAuthorSitemap(Sitemap):
    changefreq = 'Hourly'
    priority = 0.8

    def items(self):
        return Quote.objects.all()
    
    def location(self, obj):
        return reverse('display_quotes_authors', args=[obj.id,obj.author.id])




