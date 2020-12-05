# React-Django-Heroku Web App Deployment

## Introduction

This is a simple Todo web application built using React.js (front-end) and Django (back-end).

There are mainly two ways you can deploy this kind of web app:

1. **Separating Back-end and Front-end:**
   In this method, you server your back-end and front-end apps separately and they connect to each other with their respective URIs. One major overead of this approach is you have to configure CORS yourself. If you don't know about CORS you can learn more here.

   In this project, we will be using this method

2. **Serving from the same host:**
   In this method you will be serving the app from the same URI so it removes the CORS overhead. Also, it makes it easier to maintain smaller-medium sized apps. You don't want to create two separate repositories for some simple sites like a blog, to-do etc.

   This method requires building the React app first (npm run build) and update both the Django views (views.py) and urls (urls.py) to render the index.html template directly

## Technology Stack

### Front-end
* react@17.0.1
    * react-dom@17.0.1
* axios@0.21.0
* bootstrap@4.5.3
* reactstrap@8.7.1
### Back-end
* Django==3.1.3
    * djangorestframework==3.12.2
    * django-cors-headers==3.5.0
    * dj-database-url==0.5.0
    * django-heroku==0.3.1
* gunicorn==20.0.4
* whitenoise==5.2.0
* python-dotenv==0.15.0
* psycopg2==2.8.6
* psycopg2-binary==2.8.6

## Prerequisites

### 1. Install Node.js
Download Node.js and Node Package Manager (NPM) **[here](https://nodejs.org/en/)**.

### 2. Set up Virtual Environment

a. Using venv (preferred)

- To **create** virtual environment:
    ```Shell
    $ python3 -m venv venv
    ``` 
- To **activate** virtual environment (Linux/Mac OS):
    ```Shell
    $ source venv/bin/activate
    ``` 

b. Using pipenv

- Install pipenv:
    ```Shell
    $ pip install pipenv # Python 2
    $ pip3 install pipenv # Python 3
    ``` 
- Enter virtual environment shell:
    ```Shell
    $ pipenv shell
    ``` 

## Setting up the Backend

### 1. Create new project directory

```
$ mkdir (DIR_NAME)
$ cd (DIR_NAME)
``` 

### 2. Install dependencies
Run the following command inside your virtual environment:

- Using pipenv:
    ```Shell
    $ pipenv install -r requirements.txt # (Python 2)
    $ pipenv3 install -r requirements.txt # (Python 3)
    ``` 
- Using venv:
    ```Shell
    $ pip install -r requirements.txt # (Python 2)
    $ pip3 install -r requirements.txt # (Python 3)
    ``` 

### 3. Create new Django project
Run the following command inside your virtual environment:
```Shell
$ django-admin startproject backend
``` 

### 4. Extract all Django project files to parent directory (recommended)
The directory should look as follows:
```
.
├── README.md
├── backend
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
```

### 5. Create new Django app
First, navigate into the newly created backend folder. Then, start a new Django app. We will also run migrations and start up the server:
```Shell
$ cd backend
$ python manage.py startapp todo
$ python manage.py migrate
$ python manage.py runserver
``` 

If everything works well, we should see an instance of a Django application running on this address — http://localhost:8000

![alt text](https://scotch-res.cloudinary.com/image/upload/v1542486456/ia8jlkozut4uxwatnqwp.png)
### 5. Register new Django app

Open the backend/settings.py file and update the INSTALLED_APPS section as so:
```Python
# backend/settings.py

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo' # Add this
]
``` 

### 5. Set up the APIs

In order to allow for API CRUD operations between both front and back end, we need to utilise the **Django REST Framework** as well as **Django CORS Headers**.

Django REST framework is a powerful and flexible toolkit for building Web APIs, while Django CORS Headers is a Django app for handling the server headers required for Cross-Origin Resource Sharing (CORS).