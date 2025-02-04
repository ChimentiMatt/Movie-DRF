# Movie-DRF

A Django REST Framework project for managing movies, running in Docker.

---

## 🚀 Getting Started

### Prerequisites
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop).

---

## 🔧 Setup

1. Clone the repository:
   git clone https://github.com/yourusername/Movie-DRF.git
   cd Movie-DRF

2. Create a `.env` file based on `.env.example`:
```
   SECRET_KEY=your-secret-key
   DB_NAME=postgres
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_HOST=db
   DB_PORT=5432
```
---

## ▶️ Running the Project

1. **Start Docker Desktop** and ensure the Docker Engine is running.

2. Start the Docker containers:
   docker-compose up -d

3. Access the app:
   - **Homepage**: http://localhost:8000/
   - **Admin Panel**: http://localhost:8000/admin/

---

## 🔧 Common Commands

- **Apply Migrations**:
   docker-compose exec web python manage.py migrate

- **Create a Superuser**:
   docker-compose exec web python manage.py createsuperuser

- **View Logs**:
   docker-compose logs web

- **Stop Containers**:
   docker-compose down

---

## 🛠️ Development Notes

- Make sure `.env` is not tracked in version control. Use `.gitignore` to exclude it.
- Use `docker-compose.override.yml` for local development configurations if needed.

---
