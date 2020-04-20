from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('repos/', views.repos, name='repos'),
    path('logout', views.logout, name='logout'),
    # path('gitrepo/$', views.gitrepo, name='gitrepo')
]
