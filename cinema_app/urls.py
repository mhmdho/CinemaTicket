from django.urls import path
from .views.auth_views import login_view, logout_view
from .views.booking_views import home, showtimes, select_seat, book_seat
# from .views.api_views import BookSeatAPI
from .views.ticket_views import view_tickets_summary
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('room/<int:room_id>/', showtimes, name='showtimes'),
    path('showtime/<int:showtime_id>/', select_seat, name='select_seat'),
    path('book/<int:showtime_id>/<int:row>/<int:seat>/', book_seat, name='book_seat'),
    # path('api/book/<int:showtime_id>/<int:row>/<int:seat>/', BookSeatAPI.as_view(), name='api_book_seat'),
    path('tickets/<int:showtime_id>/', view_tickets_summary, name='view_tickets_summary'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
