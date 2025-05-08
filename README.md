# RESTful API Portfolio Project

This project is a Django REST API for managing inventory items with full CRUD operations, token-based authentication, and Swagger docs. It’s designed for both local development and easy deployment on [Render](https://render.com).

---

## Features

- CRUD endpoints for items (`/api/items/`)
- Swagger/OpenAPI docs at `/api/docs/`
- Token Authentication support
- Django Admin panel at `/admin/`
- Deployment-ready for Render.com

---

## Technologies Used

- Python 3
- Django 4
- Django REST Framework
- drf-yasg (Swagger documentation)
- Gunicorn (production WSGI)
- SQLite (default DB)

---

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/dev-pavelreuk/RESTful-API.git
cd RESTful-API
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the server

```bash
python manage.py runserver
```

Visit:

- [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)
- [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
- [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Deploying to Render.com

### 1. Add a new Web Service on [render.com](https://render.com)

- **Build Command:**
  ```bash
  pip install -r requirements.txt && ./build.sh
  ```

- **Start Command:**
  ```bash
  gunicorn project.wsgi:application
  ```

- **Environment Variables:**
  ```
  ALLOWED_HOSTS=your-subdomain.onrender.com
  SECRET_KEY=generate-a-secure-key
  DEBUG=False
  ```

> You can generate a Django `SECRET_KEY` by running:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 2. Example `build.sh` script:

```bash
#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
```

Make sure it’s executable:

```bash
chmod +x build.sh
```

---

## Project Structure

```
project/
│
├── api/                  # Django app for items
├── project/              # Main project settings and WSGI
├── requirements.txt      # Python dependencies
├── build.sh              # Render build script
├── manage.py             # Django CLI
└── README.md             # This file
```
