from django.db import models

# Create your models here.
class Visits(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Visits: {self.count}"
    
    class Meta:
        verbose_name_plural = "Visits"

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    visit_time = models.DateTimeField(auto_now_add=True)  # Automatically store the time of the visit

    def __str__(self):
        return f"{self.ip_address} visited at {self.visit_time}"