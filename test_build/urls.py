from django.urls import path
from. import views

urlpatterns=[
    path('',views.home),
    path('OCR/',views.OCR,name='OCR')

]