from django.urls import path
from .views import CorporationListCreateAPIView
from .views import CorporationUpdateDeleteAPIView

app_name = "corporations"
urlpatterns = [
    path("corporations/", CorporationListCreateAPIView.as_view(), name="corporation-create-read"),
    path("corporations/<int:pk>", CorporationUpdateDeleteAPIView.as_view(), name="corporation-update-delete"),
]
