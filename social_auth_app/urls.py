from django.urls import include, path
from allauth.socialaccount.providers.github import views as github_views

from . import views

urlpatterns = [
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('', include('dj_rest_auth.urls')),

    # GitHub
    path('github/', views.GitHubLoginView.as_view(), name='github_login'),
    path('github/callback/', views.github_callback, name='github_callback'),
    path('github/url/', github_views.oauth2_login),

    # Facebook
    path('facebook/', views.FacebookLoginView.as_view(), name='facebook_login'),

    # User
    path('current_user/', views.current_user),
    path('users/', views.UserList.as_view()),
    path('list_users/', views.get_users),
]