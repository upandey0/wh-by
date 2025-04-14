# 🏥 Healthcare Project (Django + PostgreSQL)

A Django-based Healthcare Management System with four apps:
- `doctors`
- `patients`
- `mappings`
- `users`

## 📚 Tech Stack

- Django 5.2
- Django REST Framework
- Simple JWT (JSON Web Token Authentication)
- PostgreSQL
- Python Virtual Environment (venv)
- Postman (for API testing)

## 📁 Project Structure


## ⚙️ Setup Instructions

### 📥 1. Clone the Repository

```bash
git clone https://github.com/upandey0/wh-by
cd healthcare_project
## On Windows : 
python -m venv healthcare_env
healthcare_env\Scripts\activate

## On Mac/Linux : 
python3 -m venv healthcare_env
source healthcare_env/bin/activate

## Install Dependencies :

pip install -r requirements.txt

## Create a .env file :
SECRET_KEY=abc1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
DEBUG=True
DB_NAME=healthcare
DB_USER=new_user
DB_PASSWORD=root
DB_HOST=localhost
DB_PORT=5432

## Open pgAdmin 4 or psql and run:
CREATE USER new_user WITH PASSWORD 'root';
ALTER ROLE new_user SUPERUSER CREATEDB CREATEROLE LOGIN;
CREATE DATABASE healthcare OWNER new_user;

## Run Migrations : 
python manage.py makemigrations
python manage.py migrate

## Run the Dev Server : 
python manage.py runserver
```


📬 API Testing with Postman <br>
📝 1. Open Postman

📤 2. Import the Collection

    Open Postman.

    Click Import in the top-left.

    Select Upload Files and choose the test.json file from the project directory.

    Click Import.

▶️ 3. Run the APIs

    Ensure your Django server is running: http://localhost:8000

    Use the collection to test the available APIs for:

        User registration/login

        Doctors, patients, mappings CRUD operations

    Set the authorization header with the JWT token where required.
I

