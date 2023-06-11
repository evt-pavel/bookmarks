from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('', views.dashboard, name='dashboard'),
     path('', include('django.contrib.auth.urls')),
     path('register/', views.register, name='register'),
     path('edit/', views.edit, name='edit'),
     path('social-auth/', include('social_django.urls', namespace='social')),
     path('users/', views.user_list, name='user_list'),
     path('users/follow/', views.user_follow, name='user_follow'),
     path('users/<username>/', views.user_detail, name='user_detail'),
     
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
