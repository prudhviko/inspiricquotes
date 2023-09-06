from django.contrib import admin
from .models import Category,Language,Quote,Tag,Author

admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Quote)
admin.site.register(Tag)
admin.site.register(Author)
