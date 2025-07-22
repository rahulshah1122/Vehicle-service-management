from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.unified_login, name='unified_login'),
    # ...other urls...
]