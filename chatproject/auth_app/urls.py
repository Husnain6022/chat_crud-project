from django.urls import path
from .views import SignUpView, signup_view, signin_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # API-based sign-up
    path('signup/', SignUpView.as_view(), name='signup'),

    # JWT token obtain and refresh
    path('signin/', TokenObtainPairView.as_view(), name='signin'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Template-based views
    path('template/signup/', signup_view, name='template-signup'),  # Template-based sign-up
    path('template/signin/', signin_view, name='template-signin'),  # Template-based sign-in
]
