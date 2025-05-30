from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..models import Room, Showtime, Booking

@login_required(login_url='login')
def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})

@login_required(login_url='login')
def showtimes(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    showtimes = Showtime.objects.filter(room=room).order_by('start_time')
    return render(request, 'showtimes.html', {'room': room, 'showtimes': showtimes})

@login_required(login_url='login')
def select_seat(request, showtime_id):
    showtime = get_object_or_404(Showtime, id=showtime_id)
    room = showtime.room
    total_rows = room.rows
    seats_per_row = room.seats_per_row

    booked_seats = Booking.objects.filter(showtime=showtime)
    expired_bookings = [b for b in booked_seats if b.is_expired()]
    
    # Delete expired bookings
    for booking in expired_bookings:
        booking.delete()

    booked_coords = {}
    for b in Booking.objects.filter(showtime=showtime):
        booked_coords[(b.seat_row, b.seat_number)] = b.user == request.user

    grid = []
    for row in range(1, total_rows + 1):
        row_seats = []
        for seat_num in range(1, seats_per_row + 1):
            is_booked = (row, seat_num) in booked_coords
            is_mine = booked_coords.get((row, seat_num), False)
            row_seats.append({
                'row': row,
                'number': seat_num,
                'booked': is_booked,
                'is_mine': is_mine
            })
        grid.append(row_seats)

    has_booked_seats = any(seat['is_mine'] for row in grid for seat in row)

    return render(request, 'seats.html', {
        'grid': grid,
        'showtime': showtime,
        'room': room,
        'has_booked_seats': has_booked_seats
    })

@login_required(login_url='login')
def book_seat(request, showtime_id, row, seat):
    showtime = get_object_or_404(Showtime, id=showtime_id)
    user = request.user

    # already booked seats by the current user
    booking = Booking.objects.filter(
        showtime=showtime,
        seat_row=row,
        seat_number=seat,
        user=user
    ).first()

    if booking:
        # unbooking seats by the user
        booking.delete()
    else:
        # seats booked by others
        if Booking.objects.filter(
            showtime=showtime,
            seat_row=row,
            seat_number=seat
        ).exists():
            # Seat is taken by another user – do nothing or show message
            pass
        else:
            # Book seats
            Booking.objects.create(
                user=user,
                showtime=showtime,
                seat_row=row,
                seat_number=seat
            )

    return redirect('select_seat', showtime_id=showtime_id)
