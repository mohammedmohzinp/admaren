
from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
  
urlpatterns = [
    path('login', jwt_views.TokenObtainPairView.as_view(), name ='login'),
    path('Overview/', views.Overview.as_view(), name ='Overview'),
    path('AddSnippet/', views.AddSnippet.as_view(), name ='AddSnippet'),
    path('SnippetDetails/', views.SnippetDetails.as_view(), name ='SnippetDetails'),
    path('SnippetUpdate/', views.SnippetUpdate.as_view(), name ='SnippetUpdate'),
    path('SnippetDelete/', views.SnippetDelete.as_view(), name ='SnippetDelete'),
    path('TagList/', views.TagList.as_view(), name ='TagList'),
    path('TagDeatils/', views.TagDeatils.as_view(), name ='TagDeatils'),


]