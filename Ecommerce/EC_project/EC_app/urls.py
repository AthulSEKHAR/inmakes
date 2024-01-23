
from django.urls import path

from . import views
app_name='EC_app'
urlpatterns = [
    path('', views.allprodcat, name='allpdcat'),
    path('<slug:c_slug>/', views.allprodcat, name='procat'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='proDetail'),

]