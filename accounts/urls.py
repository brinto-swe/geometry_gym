from django.urls import path
from .views import RegisterView, UserRegisterView, ActivateView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('user-register/', UserRegisterView.as_view(), name='user-register'),
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name='activate'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
