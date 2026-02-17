"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing,name='landing'),
    path('login/',views.login,name='login'),
    path('admin_panel/',views.admin_panel,name='admin_panel'),
    path('add_department/',views.add_department,name='add_department'),
    path('show_department/',views.show_department,name='show_department'),
    
    
    
    
    path('logout/',views.logout,name='logout'),
    path('deptdata/',views.deptdata,name='deptdata'),
    path('empdata/',views.empdata,name='empdata'),
    path('querydata/',views.querydata,name='querydata'),
    path('donequerydata/',views.donequerydata,name='donequerydata'),
    path('dept_count/',views.dept_count,name='dept_count'),
    path('emp_count/',views.emp_count,name='emp_count'),
    path('query_count/',views.query_count,name='query_count'),
    
    
    
    
]








