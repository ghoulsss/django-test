from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')


urlpatterns = [
    path('', views.index, name='name'),  # # http://127.0.0.1:8000
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),   # http://127.0.0.1:8000/cats/2/
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),   # http://127.0.0.1:8000/cats/dsadad/
    path('archive/<year4:year>/', views.archive, name='archive'),
]








