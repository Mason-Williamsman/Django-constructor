from django.urls import path

from . import views

app_name = 'base_console'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'), # http://django-constructor.com:8006/console/
    path('', views.dashboard_bricks_view, name='index'),
    path('index2/', views.index2_view, name='index2'),
    #path('<int:pk>/', views.ProjectCreationView.as_view(), name='create_project'),
    # path('create_project/', views.ProjectCreationView.as_view(), name='create_project'),
    path('create_project/', views.project_creation_view, name='create_project'),
    # path('project/<int:pk>/', views.ProjectCreationView.as_view(), name='project'),
    path('app_creation/', views.app_creation_view, name='app_creation'), # http://django-constructor.com:8006/console/app_creation/
]