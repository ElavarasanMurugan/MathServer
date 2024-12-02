from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('poweroflamb/',views.findpower,name="poweroflamb"),
    path('',views.findpower,name="poweroflambroot")
]