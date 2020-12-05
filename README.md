# Ray's Todo App

## Introduction

This is a simple Todo web application built using React.js (front-end) and Django (back-end).

off Django (including the Django REST Framework for API CRUD operations) and React. 

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
    ```
    python3 -m venv venv
    ``` 
- To **activate** virtual environment (Linux/Mac OS):
    ```
    source venv/bin/activate
    ``` 

b. Using pipenv

- Install pipenv:
    ```
    pip install pipenv # Python 2
    pip3 install pipenv # Python 3
    ``` 
- Enter virtual environment shell:
    ```
    pipenv shell
    ``` 

### 3. Install requirements
Run the following command inside your virtual environment:
```
pip install -r requirements.txt # (Python 2)
pip3 install -r requirements.txt # (Python 3)
``` 