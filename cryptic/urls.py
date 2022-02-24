# from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.urls import path, re_path
from django.urls.conf import include 
from django.contrib import admin
from accounts.views import leaderboard, home, rules, register
from questions.views import Hunt
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name = "accounts"
urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('register/',register, name="register"),
    path('leaderboard/',leaderboard, name="leaderboard"),
    path('hunt/',Hunt.as_view(), name='hunt'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name = 'login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'home.html'),name='logout'),
    path('',home, name='home'),
    path('rules/',rules, name="rules"),
    # path("password-reset/", auth_views.PasswordResetView.as_view(template_name='user/password_reset.html', html_email_template_name = 'user/password_reset_email.html' ), name="password_reset"), 
    # path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name="password_reset_done"),
    # path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name="password_reset_confirm"),
    # path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name="password_reset_complete"),
    # path('emailVerification/<uidb64>/<token>',activate, name='emailActivate'),
    # path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',activate, name='activate'), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
