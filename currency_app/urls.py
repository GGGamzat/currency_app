from django.contrib import admin
from django.urls import path
from translator import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/rates/', views.rates_view),
]