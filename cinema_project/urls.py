"""
URL configuration for STD_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from cinema_app.views.api_views import BookSeatAPI
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from cinema_app.views.api_views import RoomListAPI, RoomMovieListAPI, UserTicketListAPI


router = DefaultRouter()
router.register(r'books', BookSeatAPI, basename='book')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cinema_app.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),    
    path('api/book/<int:showtime_id>/<int:row>/<int:seat>/', BookSeatAPI.as_view(), name='api_book_seat'),
    path('api/rooms/', RoomListAPI.as_view(), name='api_room_list'),
    path('api/rooms/<int:room_id>/movies/', RoomMovieListAPI.as_view(), name='api_room_movies'),
    path('api/tickets/', UserTicketListAPI.as_view(), name='api_user_tickets'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
