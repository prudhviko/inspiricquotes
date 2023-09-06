from .models import Author, Language, Category

def common_data(request):
    authors = Author.objects.all()
    languages = Language.objects.all()
    categories = Category.objects.all()
    return {
        'authors': authors,
        'languages': languages,
        'categories': categories
    }
