from django.urls import re_path

from Publications import views

urlpatterns = [
    re_path(r"^publications/submit/$", views.submit_publication, name='submit_publication'),
    re_path(r"^publications/lookup/$", views.lookup_publication, name='lookup_publication'),
    re_path(r"^publications/", views.publications_view, name='publications'),
]
