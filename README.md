# 🎬 Movie API & IMDb-Like Web App

A project initiated on **February 4th**, designed to be a **strong portfolio piece**, showcasing expertise in backend development, API design, and full-stack integration.

## 📌 MVP Goals
- **Migrate** over **350,000 rows** of CSV data from the **TMDB Movie Dataset** ([Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)).
- **Develop a fast, well-structured API** for movie data, including movies, cast, crew, ratings, and metadata.
- **Build an IMDb-style web app interface** to showcase frontend integration.
- **Implement a user system** that allows actors to link their profiles if they are listed in the database.
- **Automate population of API with new movies/actors** Daily populate the database with new data so that new movies and actors can be present in the API and Web app and the Dashboard of the web app can be topical.
- **Deploy on AWS** for scalability and real-world deployment experience.

## 🚀 Post-MVP Features
- 🔹 **Implement Machine Learning**: Use **linear regression** to power a **recommendation system** and enhance the "like" system while learning more about **ML applications**.
- 🔹 **Comprehensive Test Coverage**
- 🔹 **Expand functionality** with additional features (to be determined).

More updates to come! 🚀


### This repo was created from my own Django Vue Template that for now is included below






# Full Stack Docker Template

A Dockerized Full Stack setup with Django REST Framework (DRF) for the backend and a Vite-based frontend.

---

🛠️ Version Information
- Docker: 27.4.0
- Python: 3.13.1
- Node.js: 20.17.0
- Django: 4.0 or higher
- Vite: 6.0.11

## 🚀 Getting Started

### Prerequisites
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop).
- Python: Version 3.13.1 or higher (required for the Django backend)
- Node.js: Version 20.17.0 or higher (required for the Vite frontend)
---

## 🔧 Setup

1. Clone the repository:
   git clone https://github.com/ChimentiMatt/fullstack-docker-template.git
   cd fullstack-docker-template

2. Create a `.env` file based on `.env.example`:
   SECRET_KEY=your-secret-key
   DB_NAME=postgres
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_HOST=db
   DB_PORT=5432

---

## ▶️ Running the Project

1. **Start Docker Desktop** and ensure the Docker Engine is running.

2. Start the Docker containers:
   docker-compose up -d

3. Access the app:
   - **Frontend**: http://localhost:3000/
   - **Backend API**: http://localhost:8000/
   - **Admin Panel**: http://localhost:8000/admin/

---

## 🔧 Common Commands

- **Apply Migrations**:
   docker-compose exec backend python manage.py migrate

- **Create a Superuser**:
   docker-compose exec backend python manage.py createsuperuser

- **View Backend Logs**:
   docker-compose logs backend

- **View Frontend Logs**:
   docker-compose logs frontend

- **Stop Containers**:
   docker-compose down

---

## 🛠️ Development Notes

- Ensure `.env` is **not tracked** in version control. Use `.gitignore` to exclude it.
- Use `docker-compose.override.yml` for local development configurations if needed.
- The frontend is built using **Vite**, and the backend is powered by **Django REST Framework**.

---

## 📂 Project Structure
```
fullstack-docker-template/
├── backend/        # Django backend (formerly movieproject)
│   ├── backend/    # Django project files
│   ├── manage.py   # Django CLI
│   ├── requirements.txt
│   ├── Dockerfile  # Backend Docker setup
│   └── ...
├── frontend/       # Frontend (Vite + React or Vue)
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── Dockerfile  # Frontend Docker setup
│   └── ...
├── docker-compose.yml  # Docker configuration
├── .env.example   # Environment variables template
└── README.md      # Project documentation
```
---
Created by Matthew Chimenti: ChimentiMatt


# Notes
docker exec -it backend sh
docker exec -it backend python manage.py makemigrations

docker-compose down
docker-compose up --build

docker-compose down
docker-compose up

docker-compose restart backend

docker-compose logs -f


can get celeb pics from wikipedia 
https://en.wikipedia.org/w/api.php?action=query&titles=Robin_Williams&prop=pageimages&format=json&pithumbsize=500

response will have source with url