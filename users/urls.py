from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('reset', views.reset),
    path('forgetpassword', views.forgetpassword)

    # path('reset_password/',
    #      auth_views.PasswordResetView.as_view(template_name="shop/password_reset.html"),
    #      name="reset_password"),

    # path('reset_password_sent/',
    #      auth_views.PasswordResetDoneView.as_view(template_name="shop/password_reset_sent.html"),
    #      name="password_reset_done"),

    # path('reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(template_name="shop/password_reset_form.html"),
    #      name="password_reset_confirm"),

    # path('reset_password_complete/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name="shop/password_reset_done.html"),
    #      name="password_reset_complete"),

]