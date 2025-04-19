from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views
from users.views import SubscriptionToggleAPIView

urlpatterns = [
    path('payments/', views.PaymentsListAPIView.as_view(), name='payments'),
    path('subscribe/', SubscriptionToggleAPIView.as_view(), name='course-subscribe'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # вход
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # обновление
]