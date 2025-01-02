# from django.urls import path
# from . import views

# urlpatterns = [
  
#     # this path are built later
#     path('' ,views.posts_lists , name = 'post'),
#     path('posts/<slug:slug>' ,views.post_page , name = 'page'),

# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_lists, name='posts'),
    path('<slug:slug>', views.post_page, name='page')
]
