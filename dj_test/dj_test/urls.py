from django.contrib import admin
from django.urls import path, include

# # Create a simple health check view
# def health_check(request):
#     return HttpResponse('<h3>Health Check: OK</h3>')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('health', health_check), # Add the health check URL
    path('', include('visits.urls')), # Add the URL pattern for the visits app
]
