from django.urls import path

from .views import create_corp_view
from .views import update_corp_view
from .views import delete_corp_view

app_name = 'corporations'
urlpatterns = [
    path('create/', create_corp_view, name="create-corp"),
    path('<int:pk>/update/', update_corp_view, name="update-corp"),
    path('<int:pk>/delete/', delete_corp_view, name="delete-corp")
]