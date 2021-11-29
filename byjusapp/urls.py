from django.urls import path
from . import views

urlpatterns=[
        path('signup/', views.fnsign, name='signup'),
        path ('model/',views.fnmodel, name='model')
]