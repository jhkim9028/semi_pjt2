from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:user_pk>/follow/", views.follow, name="follow"),
    path("<int:pk>/block/", views.block, name="block"),
    path("block_user/", views.block_user, name="block_user"),
    path("<int:pk>/block_user_block/", views.block_user_block, name="block_user_block"),
    path("password/", views.password, name='password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_dont"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('<int:user_pk>/pay_history', views.pay_history, name="pay_history"),
]