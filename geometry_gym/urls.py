from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(title="Geometry Gym API", default_version='v1', description="Geometry Gym API docs"),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),

    # Djoser authentication (users, activation, jwt create/refresh)
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),

    # app endpoints
    path('api/memberships/', include('memberships.urls')),
    path('api/classes/', include('classes.urls')),
    path('api/bookings/', include('bookings.urls')),
    path('api/attendance/', include('attendance.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/feedback/', include('feedback.urls')),
    path('api/reports/', include('reports.urls')),


    # Swagger / Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]