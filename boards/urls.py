from . import views
from django.urls import path


urlpatterns = [

path('',views.BoardListView.as_view(), name='home'),
path('boards/<int:pk>/',views.TopicListView.as_view(),name='board_topics'),
path('boards/<int:pk>/new/',views.new_topic,name='new_topic'),

]