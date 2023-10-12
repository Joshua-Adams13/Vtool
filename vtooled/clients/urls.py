from django.urls import path

from . import views

app_name = "clients"
urlpatterns = [
    #  /clients/
    path("", views.IndexView.as_view(), name="index"),
    path("details/", views.DetailsView.as_view(), name="details"),
    path("sign_up/", views.SignUpView.as_view(), name="sign_up"),
]