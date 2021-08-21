from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.feed, name='feed'),
    path('category/', views.category, name='category'),
    path('about-us/', views.about, name='about'),
    path('get-started/', views.get_started, name='get-started'),
    path('category/<slug:slug>/', views.category_post, name='category_post'),
    path('<slug:category_slug>/<slug:slug>/', views.post_detail, name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)