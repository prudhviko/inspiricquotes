from .models import Quote,Author,Language,Category
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.http import HttpResponse

def custom_404(request, exception):
    return render(request, "404.html",status=404)

def home(request):
    quotes = Quote.objects.all()
    paginator = Paginator(quotes, 18)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    context = {'objects': objects}
    return render(request, 'home.html', context)

def quotes(request, id):
    current_quote = get_object_or_404(Quote, id=id)
    previous_quote = Quote.objects.filter(id__lt=id).order_by('-id').first()
    next_quote = Quote.objects.filter(id__gt=id).order_by('id').first()
    context = {
        'quote': current_quote,
        'previous_quote': previous_quote, 
        'next_quote': next_quote,
    }
    return render(request, 'quotes.html', context)


def quotes_by_authors(request,id,name):
    quotes = Quote.objects.filter(author__id=id)
    paginator = Paginator(quotes, 18)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    author_name = Author.objects.filter(id=id).first()
    all_authors = Author.objects.exclude(id=id)
    context = {
        'objects': objects,
        'all_authors': all_authors,
        'author_name': author_name
    }
    return render(request,'quotes_by_authors.html',context)

def display_quotes_authors(request,author_id,quote_id):
    quote = get_object_or_404(Quote, id=quote_id, author_id=author_id)
    prev_quote = Quote.objects.filter(author_id=author_id, id__lt=quote.id).order_by('-id').first()
    next_quote = Quote.objects.filter(author_id=author_id, id__gt=quote.id).order_by('id').first()
    all_authors = Author.objects.exclude(id=author_id)
    context = {
        'quote': quote,
        'prev_quote': prev_quote,
        'next_quote': next_quote,
        'all_authors': all_authors,
    }
    return render(request, 'display_quotes_authors.html', context)

def quotes_by_languages(request,id,name):
    quotes = Quote.objects.filter(language__id=id)
    paginator = Paginator(quotes, 18)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    language_name = Language.objects.filter(id=id).first()
    all_languages = Language.objects.exclude(id=id)
    meta_title = language_name.meta_title
    meta_description = language_name.meta_description
    context = {
        'objects': objects,
        'all_languages': all_languages,
        'language_name': language_name,
        'meta_title': meta_title,
        'meta_description': meta_description
    }
    return render(request,'quotes_by_languages.html',context)

def display_quotes_languages(request,quote_id,language_id):
    quote = get_object_or_404(Quote, id=quote_id, language_id=language_id)
    prev_quote = Quote.objects.filter(language_id=language_id, id__lt=quote.id).order_by('-id').first()
    next_quote = Quote.objects.filter(language_id=language_id, id__gt=quote.id).order_by('id').first()
    all_languages = Language.objects.exclude(id=language_id)
    language_name = Language.objects.filter(id=language_id).first()
    meta_title = language_name.meta_title
    meta_description = language_name.meta_description
    context = {
        'quote': quote,
        'prev_quote': prev_quote,
        'next_quote': next_quote,
        'meta_title': meta_title,
        'meta_description': meta_description,
        'all_languages': all_languages,
    }
    return render(request, 'display_quotes_languages.html', context)

def quotes_by_categories(request,id,name):
    quotes = Quote.objects.filter(category__id=id)
    paginator = Paginator(quotes, 18)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    all_categories = Category.objects.exclude(id=id)
    category_name = Category.objects.filter(id=id).first()
    meta_title = category_name.meta_title
    meta_description = category_name.meta_description
    context = {
       'objects': objects,
       'all_categories': all_categories,
       'category_name': category_name,
       'meta_title': meta_title,
       'meta_description': meta_description
    }
    return render(request,'quotes_by_categories.html',context)

def display_quotes_categories(request,quote_id,category_id):
    quote = get_object_or_404(Quote, id=quote_id, category_id=category_id)
    prev_quote = Quote.objects.filter(category_id=category_id, id__lt=quote.id).order_by('-id').first()
    next_quote = Quote.objects.filter(category_id=category_id, id__gt=quote.id).order_by('id').first()
    all_categoires = Category.objects.exclude(id=category_id)
    category_name = Category.objects.filter(id=category_id).first()
    meta_title = category_name.meta_title
    meta_description = category_name.meta_description
    context = {
       'quote': quote,
       'prev_quote': prev_quote,
       'next_quote': next_quote,
       'all_categories': all_categoires,
       'meta_title': meta_title,
       'meta_description': meta_description
    }
    return render(request, 'display_quotes_categories.html', context)

def about(request):
    return render(request,'about.html')

def privacy_policy(request):
    return render(request,'privacy-policy.html')

def terms_conditions(request):
    return render(request,'terms-conditions.html')

def support_us(request):
    return render(request,'support-us.html')

def refund_policy(request):
    return render(request,'refund-policy.html')
   


