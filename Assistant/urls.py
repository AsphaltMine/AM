from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r"^assistant/chat/$", views.chat, name="assistant_chat"),
]
