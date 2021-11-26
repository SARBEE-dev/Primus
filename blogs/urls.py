from django.urls import path
from django.conf import settings
from django.conf.urls import static
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,\
    UserPostListView, CreateComment, CommentDetailView, EventDetailView, EventCreateView,\
    EventListView,EventUpdateView, EventDeleteView
urlpatterns = [path('home/', PostListView.as_view(), name='home'),
            path('', views.index, name='primus'),
            path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
            path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
            path('post/new/', PostCreateView.as_view(), name='create-view'),
            path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update-view'),
            path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
               path('about', views.about, name='about'),
               path('comment/new/', CreateComment.as_view(), name='create-comment'),
path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
path('Primusevents/', EventListView.as_view(), name='primus_events'),
path('Primus/<int:pk>/event/',EventDetailView.as_view(), name='events_detail'),
path('event/new/', EventCreateView.as_view(), name='create-event'),
path('event/<int:pk>/update/event/', EventUpdateView.as_view(), name='update-event'),
path('event/<int:pk>/delete/event/', EventDeleteView.as_view(), name='delete-event'),
               ]



