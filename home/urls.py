from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('database/', views.database, name="database"),
    path('handlelogin/', views.handlelogin, name="handlelogin"),
    path('handlelogout/', views.handlelogout, name="handlelogout"),
    path('database/', views.database, name="database"),
    path('editData/', views.editData, name="editData"),
    path('deletedata/<str:name>/', views.deletedata, name="deletedata"),
    path('error/', views.error, name="error"),
]
