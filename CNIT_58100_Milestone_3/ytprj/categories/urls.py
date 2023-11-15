from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('categories/', views.categories_view, name='categories'),
]