"""myDJ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myDJ import views, select1, Visualizing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login1/', views.login1),
    path('login/', views.login),
    path('search1/', views.search1),
    path('register1/', views.register1),
    path('register/', views.register),
    path('page/', views.page),
    path('search_word/', select1.search_by_word),
    path('BS/',views.bs),
    path('order/',views.order),
    path('apply/',views.apply),
    path('dp_active/',views.dp_active),
    path('apply1/',views.apply1),
    path('schedule/',views.schedule),
    path('reach/',views.reach),
    path('reach1/',views.reach1),
    path('leave/',views.leave),
    path('leave1/',views.leave1),
    path('manager/',views.manager),
    path('manager1/',views.manager1),
    path('show/',views.show),
    path('delete/',views.delete),

    path('add/',views.add),
    path('add1/', views.add1),
    path('edit/',views.edit),
    path('anniversary_news/',views.anniversary_news),
    # path('personal_data/',views.personal_data),
    path('p_data/',views.p_data),
    path('edit1/',views.edit1),
    path('location/',Visualizing.location),



    path('hour_sum/', Visualizing.hour_sum),
    path('hour_people/', Visualizing.hour_people),
    # path('every/', Visualizing.every_top),
    path('word_colund/', Visualizing.word_colund),
    path('word_apply/', Visualizing.word_apply),
    path('word_top/', Visualizing.word_top),
    path('shuju/', Visualizing.shuju),
]
