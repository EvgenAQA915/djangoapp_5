from django.urls import path
from djangoapp.views import index, indexItem

app_name = "djangoapp"

urlpatterns = [
    # http://127.0.0.1:8000/djangoapp/
    path("", index),
    path("<int:my_id>/", indexItem, name="detail"),
    # http://127.0.0.1:8000/djangoapp/
]
