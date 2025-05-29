# cinema_app/views/ticket_views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Booking, Showtime

@login_required
def view_tickets_summary(request, showtime_id):
    showtime = get_object_or_404(Showtime, id=showtime_id)
    
    bookings = Booking.objects.filter(
        showtime=showtime,
        user=request.user
    ).order_by('seat_row', 'seat_number')

    if not bookings:
        return render(request, 'no_ticket.html')  # Optional: handle empty case

    return render(request, 'tickets_summary.html', {
        'bookings': bookings,
        'showtime': showtime,
        'movie': showtime.movie,
        'room': showtime.room,
    })