from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import Showtime, Booking, Movie, Room
from ..serializers import BookingSerializer
from drf_spectacular.utils import extend_schema
from cinema_app.serializers import RoomSerializer, MovieSerializer, BookingSerializer


@extend_schema(
    description="Book or unbook a seat for a specific showtime.",
    responses={200: BookingSerializer},
)
class BookSeatAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, showtime_id, row, seat):
        showtime = Showtime.objects.get(id=showtime_id)
        user = request.user

        booking, created = Booking.objects.get_or_create(
            user=user,
            showtime=showtime,
            seat_row=row,
            seat_number=seat
        )
        return Response(BookingSerializer(booking).data)


@extend_schema(tags=["Rooms"])
class RoomListAPI(APIView):
    @extend_schema(
        description="Get list of all cinema rooms",
        responses={200: RoomSerializer(many=True)}
    )
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)


@extend_schema(tags=["Movies"])
class RoomMovieListAPI(APIView):
    @extend_schema(
        description="Get all movies currently showing in a specific room",
        responses={200: MovieSerializer(many=True)}
    )
    def get(self, request, room_id):
        movies = Movie.objects.filter(showtime__room_id=room_id).distinct()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


@extend_schema(tags=["Tickets"])
class UserTicketListAPI(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        description="Get all tickets booked by the logged-in user",
        responses={200: BookingSerializer(many=True)}
    )
    def get(self, request):
        tickets = Booking.objects.filter(user=request.user)
        serializer = BookingSerializer(tickets, many=True)
        return Response(serializer.data)
