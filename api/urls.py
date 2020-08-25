from django.urls import path,include
from . import views


urlpatterns = [
    path('posts/', views.GetPosts.as_view()),
    path('post/<str:name_slug>', views.GetPost.as_view()),
    path('bl/', views.BlackListItems.as_view()),
    path('posts_t/', views.GetPostsByTag.as_view()),
    path('tags/', views.GetTags.as_view()),


]
