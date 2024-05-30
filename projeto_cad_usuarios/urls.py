from django.urls import path
from app_cad_usuarios import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('', views.login, name='login'),
      path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('book/<int:appointment_id>/', views.book_appointment, name='book_appointment'),
    path('profile/', views.user_profile, name='user_profile'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)