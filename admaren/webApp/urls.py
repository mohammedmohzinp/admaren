
from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from .views import SnippetsDetailView, SnippetsListView
  
urlpatterns = [
    path('login', jwt_views.TokenObtainPairView.as_view(), name ='login'),
    path('Overview/', views.Overview.as_view(), name ='Overview'),
    path('AddSnippet/', views.AddSnippet.as_view(), name ='AddSnippet'),
    path('snippets/<int:pk>/', SnippetsDetailView.as_view(), name='snippet-detail'),
    path('SnippetDetails/', views.SnippetDetails.as_view(), name ='SnippetDetails'),
    path('SnippetUpdate/', views.SnippetUpdate.as_view(), name ='SnippetUpdate'),
    path('SnippetDelete/', views.SnippetDelete.as_view(), name ='SnippetDelete'),
    path('TagList/', views.TagList.as_view(), name ='TagList'),
    path('tagDeatils/<int:pk>/', views.TagDetailView.as_view(), name ='tagDeatils'),
    path('snippets/', SnippetsListView.as_view(), name='snippet-list'),
]