from django.urls import path
from candidate import views

urlpatterns = [
    path('login/',views.calogin,name='login'),

]