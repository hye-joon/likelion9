from django.urls import path
from . import views

urlpatterns = [
    path('commentcreate/<int:post_id>', views.commentcreate, name='commentcreate'),
    path('commentupdate/<int:comment_id>', views.commentupdate, name='commentupdate'),
    path('commentdelete/<int:comment_id>', views.commentdelete, name='commentdelete'),
]