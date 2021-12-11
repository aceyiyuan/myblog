from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib.auth import views
from django.conf import settings
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/',views.LoginView.as_view(),name='login'),
    path('accounts/logout/',views.LogoutView.as_view(next_page='/blog/'),name='logout'),
    path('blog/', include('blog.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




