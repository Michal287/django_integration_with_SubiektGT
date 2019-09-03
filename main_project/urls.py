"""main_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from django.conf.urls import url
from reclamation.views import MainSideView, AboutAsView, ContactView, ManagmentView, LoginView, LogoutView, RegisterView, ReclamationView,\
    ReclamationAddView, BranchAddView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainSideView.as_view(), name="MainSideView"),
    path('about/', AboutAsView.as_view(), name="AboutAsView"),
    path('contact/', ContactView.as_view(), name="ContactView"),
    path('managment/', ManagmentView.as_view(), name="ManagmentView"),
    path('managment/add', BranchAddView.as_view(), name="BranchAddView"),
    path('login/', LoginView.as_view(), name="LoginView"),
    path('logout/', LogoutView.as_view(), name="LogoutView"),
    path('register/', RegisterView.as_view(), name="RegisterView"),
    re_path(r'^managment/branch/(?P<id>(\d)+)$', ReclamationView.as_view(), name="ReclamationView"),
    re_path(r'^managment/branch/(?P<id>(\d)+)/add$', ReclamationAddView.as_view(), name="ReclamationAddView")

]
