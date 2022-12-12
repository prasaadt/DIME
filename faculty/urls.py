from django.urls import path
from faculty import views

urlpatterns = [
    path('login/',views.facultyinputview,name='faculty login'),

]