from django.urls import path
from list import views

urlpatterns = [
    path('user_lists/', views.ListViewSet.as_view({'get':'get_user_lists'}), name='get_lists'),
    path('get_list/<int:list_id>', views.ListViewSet.as_view({'get':'get_user_list','put':'put','delete':'delete'}),name='get user list'),
    path('create/', views.ListViewSet.as_view({'post':'post'}),name='get user list'),


    path('items/<int:list_id>', views.ListItemViewSet.as_view({'get':'get_user_list_items'}), name='list items'),
    path('item/<int:item_id>', views.ListItemViewSet.as_view({'get':'get_item','put':'put','delete':'delete'}),name='get item'),
    path('item/', views.ListItemViewSet.as_view({'post':'post'}),name='get item'),
    path('items/today/', views.ListItemViewSet.as_view({'get':'get_today_user_items'}),name='get items'),


    path('item/finish/<int:item_id>', views.ListItemViewSet.as_view({'post':'finish_task'})),
    path('item/unfinish/<int:item_id>', views.ListItemViewSet.as_view({'post':'unfinish_task'})),
]