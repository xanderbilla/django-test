# Storing IP Address in SQLite

To store the IP addresses of visitors to your Django webpage in an SQLite database, follow these steps:

### 1. **Update Your Django Model**
Define a model to store the IP addresses and any other information you want to track.

```python
# models.py
from django.db import models

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    visit_time = models.DateTimeField(auto_now_add=True)  # Automatically store the time of the visit

    def __str__(self):
        return f"{self.ip_address} visited at {self.visit_time}"
```

### 2. **Create and Apply Migrations**
Run the following commands to create and apply the database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. **Capture the IP Address in the View**
Update your view to capture the IP address of the visitor and store it in the database.

```python
# views.py
from django.shortcuts import render
from .models import Visitor

def get_client_ip(request):
    """Extract the client's IP address from the request."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home(request):
    # Capture and store the visitor's IP address
    ip_address = get_client_ip(request)
    Visitor.objects.create(ip_address=ip_address)

    return render(request, 'home.html', {'ip_address': ip_address})
```

### 4. **Display or Use the Data**
Pass the IP address or related data to your template for rendering.

```html
<!-- home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visitor Info</title>
</head>
<body>
    <h1>Hello, Visitor!</h1>
    <p>Your IP Address: {{ ip_address }}</p>
</body>
</html>
```

### 5. **Run the Django Development Server**
Start the server to test the implementation:

```bash
python manage.py runserver
```

Visit your webpage, and the IP address of the visitor will be logged into the database.

### Optional Enhancements
- **Filter Duplicate IPs**: If you want to avoid duplicate entries, you can check if an IP already exists in the database before saving.
- **Add a Dashboard**: Create an admin page or a custom view to list and analyze stored IP addresses.