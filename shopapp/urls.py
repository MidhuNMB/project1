from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from shopapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('api-auth',include('rest_framework.urls')),
    path('addproduct',views.addproduct.as_view(),name='addproduct'),
    path('addstaff',views.addstaff.as_view(),name='addstaff'),
    path('viewproduct',views.viewproduct.as_view(),name='viewproduct'),
    path('deleteproduct',views.dleteproduct.as_view(),name='deleteproduct')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)