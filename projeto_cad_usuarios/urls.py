from django.urls import path
from app_cad_usuarios import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from app_cad_usuarios.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_cad_usuarios.urls')),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('', views.login, name='login'),
      path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('book/<int:appointment_id>/', views.book_appointment, name='book_appointment'),
    path('profile/', views.user_profile, name='user_profile'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
     path('login/', login_view, name='login')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)