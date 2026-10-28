from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import (
    MyTokenObtainPairView,
    UserList,
    UserRegistration,
    UserRetrieve,
    UserDestroy,
    UserUpdate,
)

app_name = "users"

urlpatterns = [
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user/list/", UserList.as_view(), name="u-list"),
    path("user/register/", UserRegistration.as_view(), name="u-register"),
    path("user/retrieve/<int:pk>/", UserRetrieve.as_view(), name="u-retrieve"),
    path("user/update/<int:pk>/", UserUpdate.as_view(), name="u-update"),
    path("user/destroy/<int:pk>/", UserDestroy.as_view(), name="u-destroy"),
]
