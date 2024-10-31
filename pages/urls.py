from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("message/", views.sendmessageview, name="sendmessage"),
    path("message/<int:id>/", views.messageview, name="message"),
    path("unauthorized/", views.unauthorizedview),
    path("register/", views.registerview),
    path("register/registeruser/", views.registeruserview),
    path("recover/", views.recoverview),
    path("recover/send/", views.sendrecover)
]