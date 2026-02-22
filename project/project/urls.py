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
    path('login/',views.login,name="login"),
    path('password_reset/',views.password_reset,name="password_reset"),
    path('reset_pass_code/',views.reset_pass_code,name="reset_pass_code"),
    path('confirm_password/',views.confirm_password,name="confirm_password"),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('add_employees/',views.add_employees,name='add_employees'),
    path('show_employee/',views.show_employee,name='show_employee'),
    path('add_department/',views.add_department,name='add_department'),
    # path('show_department',views.show_department,name='show_department'),
# ------------------------------------------------------------
    path('addemp/',views.addemp,name='addemp'),
    path('save_department/',views.save_department,name='save_department'),
# -----------------------------------------------------------------------------
    path('emppanel/',views.emppanel,name='emppanel'),
    path('add_query/',views.add_query,name='add_query'),
    path('all_queries/',views.all_queries,name='all_queries'),
    path('reply_save/',views.reply_save,name='reply_save'),
    path("employees/search/", views.search_employees, name="search_employees"),

    
    
    
]
