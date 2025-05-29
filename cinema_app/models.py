from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


# cinema_app/models.py

class Room(models.Model):
    name = models.CharField(max_length=50)
    rows = models.IntegerField(default=10)
    seats_per_row = models.IntegerField(default=8)
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)  # New line

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/')
    description = models.TextField()

    def __str__(self):
        return self.title


class Showtime(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} at {self.start_time}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seat_row = models.IntegerField()
    seat_number = models.IntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('showtime', 'seat_row', 'seat_number')

    def is_expired(self):
        return timezone.now() > self.booked_at + datetime.timedelta(minutes=10)

    def __str__(self):
        return f"Booking by {self.user.username} for seat {self.seat_row}-{self.seat_number}"
