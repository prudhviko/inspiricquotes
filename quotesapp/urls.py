from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('quotes/<int:id>',views.quotes,name='quotes'),
    path('quotes/author/<int:id>/<str:name>',views.quotes_by_authors,name='quotes_by_authors'),
    path('author/<int:author_id>/<int:quote_id>/', views.display_quotes_authors, name='display_quotes_authors'),
    path('quotes/languages/<int:id>/<str:name>',views.quotes_by_languages,name='quotes_by_languages'),
    path('languages/<int:quote_id>/<int:language_id>',views.display_quotes_languages,name='display_quotes_languages'),
    path('quotes/categories/<int:id>/<str:name>',views.quotes_by_categories,name='quotes_by_categories'),
    path('quotes/<int:quote_id>/<int:category_id>',views.display_quotes_categories,name='display_quotes_categories'),
    path('about/',views.about,name='about'),
    path('privacy-policy/',views.privacy_policy,name='privacy-policy'),
    path('terms-conditions/',views.terms_conditions,name='terms-conditions'),
    path('support-us/',views.support_us,name='support-us')
]