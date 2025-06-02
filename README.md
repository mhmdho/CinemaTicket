# 🎬 Cinema Booking App

A Django-based cinema booking system that allows users to select and book seats for showtimes in different rooms.  
This project consist of user login, admin panel and REST API support.


## ✅ Features

- Book seats per showtime
- View available and booked seats (with user-specific bookings)
- Admin portal for managing:
  - Rooms
  - Movies
  - Showtimes
- REST API endpoints with Swagger UI
- Responsive HTML templates
- Dockerized setup for easy deployment


## 🧾 Technologies Used

| Tool | Description |
|------|-------------|
| **Python** | Backend logic |
| **Django** | Web framework |
| **DRF (Django REST Framework)** | API endpoints |
| **drf-spectacular** | OpenAPI/Swagger docs |
| **PostgreSQL** | Database |
| **Gunicorn** | Production WSGI server |
| **Nginx** | Static/media file server |
| **Docker & Docker Compose** | Containerization |


## 📦 Prerequisites

Before you begin, ensure you have installed:

- [Docker](https://docs.docker.com/engine/install/) 
- [Docker Compose](https://docs.docker.com/compose/install/) 
- Python 3.10+
- PostgreSQL (for local dev if not using Docker)


## 🚀 Getting Started (Local Development)

1. **Clone the repository**

```bash
git clone https://github.com/mhmdho/CinemaTicket.git 
cd CinemaTicket
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Apply migrations**
```bash
python manage.py migrate
```

4. **Create superuser**
```bash
python manage.py createsuperuser
```

5. **Run development server**
```bash
python manage.py runserver
```

👉 Visit: http://localhost:8000/admin  
Login with your admin credentials


## 🐳 Running with Docker (Production Setup)

1. **Build and start containers (Starts all services defined in docker-compose.yml in detached mode.)**

```bash
docker-compose up -d --build
```

2. **Applies database migrations inside the running container.**

```bash
docker-compose exec web python manage.py migrate
```

3. **Collects static files into STATIC_ROOT for production use.**

```bash
docker-compose exec web python manage.py collectstatic --noinput
```

4. **Creates a new admin user inside the container.**

```bash
docker-compose exec web python manage.py createsuperuser
```

5. **Access the app:**  
👉 Visit: http://localhost:8000/  
👉 Visit: http://localhost:8000/admin/  
👉 Visit: http://localhost:8000/api/docs/  

<br>

"⚠️ For production use, set DEBUG=False and enable HTTPS via Let's Encrypt or Certbot."


## 📁 Media Uploads

All uploaded images (room images, movie posters) are stored in:

```bash
media/
├── room_images/
└── posters/
```

Ensure Nginx is configured to serve `/media/` correctly.


## 🔧 API Endpoints

Swagger UI for testing APIs:  
👉 http://localhost:8000/api/docs/

Available Endpoints:

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/rooms/` | Get all rooms |
| GET | `/api/rooms/<id>/movies/` | Get movies showing in a room |
| GET | `/api/tickets/` | Get all tickets booked by current user |
| POST | `/api/book/<showtime_id>/<row>/<seat>/` | Book or unbook a seat


## 📁 Folder Structure

```bash
cinema_project/  
├── cinema_app/                # Django app  
│   ├── models.py              # Room, Movie, Booking, etc.  
│   ├── views/  
│   │   ├── booking_views.py  
│   │   └── api_views.py  
│   ├── serializers/  
│   │   └── booking_serializer.py  
│   └── templates/  
│       ├── base.html  
│       ├── home.html  
│       ├── showtimes.html  
│       └── seats.html  
│  
├── cinema_project/  
│   ├── settings.py            # Django project settings  
│   ├── urls.py  
│   └── wsgi.py  
│  
├── staticfiles/               # Auto-generated static files (after collectstatic)  
├── media/                     # Uploaded media files  
├── manage.py  
├── Dockerfile                 # Docker build config  
├── docker-compose.yml         # Docker services definition  
├── nginx.conf                 # Nginx config for media/static  
├── requirements.txt           # Python dependencies  
└── README.md                  # This file  
```

## 🛡️ Configuration

You can configure these environment variables in `docker-compose.yml`:

| Variable | Description |
|---------|-------------|
| `DEBUG` | Set to `False` for production |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts |
| `SECRET_KEY` | Django secret key |
| `DATABASE_URL` | PostgreSQL connection string (optional) |

## 🛡️ Production Deployment
For live deployment:

- Set DEBUG=False in settings.py
- Use domain name instead of localhost
- Enable HTTPS with Let's Encrypt/Certbot
- Use environment variables for secrets
- Add monitoring and backups for PostgreSQL

## 🧪 Optional Enhancements

- Add JWT authentication for mobile apps
- Integrate with Stripe for payment
- Export tickets as PDF
- Add WebSocket support for real-time seat updates

## 💬 Support

If you encounter any issues during setup or deployment, feel free to contact me — I'm happy to help!

## 📜 License

This project is licensed under my License :).