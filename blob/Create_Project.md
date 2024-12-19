# Create a Django project

### 1. Install Django using pip

In your activated virtual environment, use one of the following:

Latest version of Django (any version)
```bash
$ pip install django
```
Latest version of Django 4.2
```bash
$ pip install "django>=4.2,<5"
```
Specific version of Django
```bash
$ pip install "django==4.2.3"
```
Install from the requirements.txt file
```bash
$ pip install —r requirements .txt
```


### 2. Create a new project using `django—admin startproject`

`$ django-admin startproject <project_name>`
This will create a new folder with project_name and the following
structure (if project name is dj_test)
```
dj _ test
    ├───`manage.py`
    └───dj_test
            ├───`__init__. py`
            ├───`settings.py`
            ├───`urls.py`
            ├───`wsgi.py`
            ├───`asgi.py` (only in Django 3+)
```
### 3. Run the development server

To run the development server (default port 8000) -

```bash
$ python manage.py runserver
```

### 4. Initialize the development database

Initialize the development database

```bash
$ python manage. py migrate
```

This will initialize a SQLite database (**`db.sqlite3`**) with the tables
specified in the default project:

- authorization tables (user, permissions, groups)
- django_migrations
- django_admin_log
- django_sessions
- django_content_type

You can edit the database type and default tables by editing the
`settings.py` file

- **`django_migrations`**
    - required for Django's ORM feature
- **authorization tables** (user, permissions, groups)
    - default user and permissions features
- **`django_admin_log`**
    - tracks changes made via the Django Admin
- **`django_sessions`**
    - used in the sessions app (e.g. cookies)
- **`django_content_type`**
    - used for generic model relations (like tags, comments, likes, etc)

#### View the data in the database

- Command line interface
- An app
    - e.g. DB Browser for SQLite or SQLiteStudio
- VS Code extension
    -   plugin: SQLite

### 5. Create a superuser

```bash
$ python manage.py createsuperuser
```
Creates your first user so that you can log into the admin site.

You supply:
- username
- email address
- password
    - You can bypass the password requirements

### 6. View the admin site

Make sure your server is running

```bash
$ python manage. py runserver
```
- Open http://127.0.0.1:8000/admin
- Log in using your superuser credentials
- You can now browse, create, edit, and delete your Django models
- Only users and groups are configured initially.
We'll add more later