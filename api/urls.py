from django.urls import path,include
from . import views


urlpatterns = [
    path('posts/', views.GetPosts.as_view()),
    path('post/<str:name_slug>', views.GetPost.as_view()),
    path('bl/', views.BlackListItems.as_view()),
    path('bl/item/<str:name_slug>', views.GetBlackListItem.as_view()),
    path('bl/filter', views.BlackListFilter.as_view()),
    path('bl/search', views.BlackListSearch.as_view()),
    path('bl/types/', views.BlackListTypes.as_view()),
    path('posts_t/', views.GetPostsByTag.as_view()),
    path('tags/', views.GetTags.as_view()),


]
