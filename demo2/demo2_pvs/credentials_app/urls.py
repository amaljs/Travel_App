from django.urls import path

from demo2_pvs.credentials_app import views

urlpatterns = [

    path('register/',views.register,name="register"),
    path('login/',views.loginuser,name='login'),
    path('logout',views.logoutuser,name='logout')

]