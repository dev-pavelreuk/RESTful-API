# RESTful API Final Application

This Django RESTful API allows users to manage items in a simple inventory. It demonstrates CRUD operations, Django REST Framework integration, and deployment.

## Features
- Create, Read, Update, Delete (CRUD) for items
- RESTful endpoints
- Automatic timestamping of item creation
- Admin dashboard support

## Technologies Used
- Python
- Django
- Django REST Framework

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
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

### 5. Create a superuser (optional for admin access)
```bash
python manage.py createsuperuser
```

### 6. Run the server
```bash
python manage.py runserver
```

### 7. Access the API
Go to: `http://127.0.0.1:8000/api/items/`
