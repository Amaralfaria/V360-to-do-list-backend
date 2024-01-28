from django.urls import path
from list import views

urlpatterns = [
    path('user_lists/', views.ListViewSet.as_view({'get':'get_user_lists'}), name='get_lists'),
    path('get_list/<int:list_id>', views.ListViewSet.as_view({'get':'get_user_list'}),name='get user list')
]