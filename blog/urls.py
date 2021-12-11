from django.urls import path

from . import views

#app_name = 'blog' #optional

urlpatterns=[
	path('',views.post_list,name='post_list'),
	path('post/<int:pk>/',views.post_detail,name="post_detail"), 
    path('post/new/',views.post_new,name='post_new'),
    path('post/<int:pk>/edit/',views.post_edit,name='post_edit'),
    path('post/drafts/',views.post_draft_list,name="post_draft_list"), #http://127.0.0.1:8000/blog/post/drafts/
    path('post/<pk>/publish/',views.post_publish,name='post_publish'),
    path('post/<pk>/remove/',views.post_remove,name='post_remove'),
    path('post/<pk>/comment/',views.add_comment_to_post, name='add_comment_to_post'), #or <int:pk>
    path('post/comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
	path('post/comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/search', views.search, name='search'),
]
