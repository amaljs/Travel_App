from django.urls import path

from demo2_app import views

urlpatterns = [

    path('',views.index,name="index"),
    path('result/',views.sult,name="result")
]