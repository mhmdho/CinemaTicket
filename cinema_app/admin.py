from django.contrib import admin
from .models import Room, Movie, Showtime, Booking
from django.utils.html import format_html


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'rows', 'seats_per_row', 'room_image')

    def room_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;">'.format(obj.image.url))
        return "-"

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Showtime)
class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ('room', 'movie', 'start_time')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'showtime', 'seat_row', 'seat_number', 'booked_at')
