# Basic Flask CRUD APP

## 1. Clone Repo

```bash
  git clone <your-repo-url>
  cd <your-project-folder>
```

## 2. Create Virtual Env

```bash
  python -m venv env
  source env/bin/activate
```

## 3. Install Dependencies

```bash
   pip install -r requirements.txt
```

## 4. Create Database in MySQL

```sql
create database flask_crud;

use flask_crud;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
);
```

## 5. Make Migrations in App

```bash
  python manage.py makemigrations students
  python manage.py migrate students
  python manage.py migrate
```

## 6. Create Super User

```bash
  python manage.py createsuperuser
```

## 7. Run Server or App

```bash
    python app.py
```

## 8. Run Server or App

```url
    http://localhost:5000
```