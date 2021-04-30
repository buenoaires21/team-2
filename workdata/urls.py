from django.urls import path
from .views import home, load_data_success, load_data_form, index
urlpatterns = [
    path("", index, name="index"),
    path("load-data/", load_data_form, name="load-data"),
    path("load-data/success/", load_data_success, name="load-data-success"),
]
