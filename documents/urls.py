from django.urls import path

urlpatterns = [
    path("documents"),
    path("documents/<id>"),
    path("fields/<id>"),
    path("export/<id>"),
]