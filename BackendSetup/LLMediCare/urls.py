from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user_session.urls')),
    path('api/ai/', include('ai_agent.urls')),
]
