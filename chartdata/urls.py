from django.urls import path

from .import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.base),
    path('chart/',views.chart,name='chart'),
    path('highchart/',views.highchart,name='highchart'),
    path('signIn',views.signIn),
    path('update_profile/<int:pk>',views.update_profile,name='update_profile'),
    path('login',auth_views.LoginView.as_view(template_name='login.html'),name='login'),

]
