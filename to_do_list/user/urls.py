from django.urls import path
from user import views

urlpatterns = [
    path('create/', views.CreateUsuarioView.as_view({'post':'post'}), name='create_usuario'),
    path('login/',views.LoginViewSet.as_view({'post':'login','get':'test_auth'}), name='login_usuario'),
]