from django.urls import path
from .views import new_chat_view, chat_view

urlpatterns = [
    path("", view=new_chat_view, name="new_chat"),
    path("<int:user_id>/<int:chat_id>", view=chat_view, name="chat"),
]
