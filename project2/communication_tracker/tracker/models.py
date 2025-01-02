# from django.db import models

# Create your models here.
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    linkedin_profile = models.URLField()
    emails = models.TextField(help_text="Comma-separated emails")
    phone_numbers = models.TextField(help_text="Comma-separated phone numbers")
    comments = models.TextField(blank=True, null=True)
    communication_periodicity = models.IntegerField(help_text="Days between communications")

    def __str__(self):
        return self.name

class CommunicationMethod(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    sequence = models.IntegerField()
    mandatory = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class CommunicationLog(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    method = models.ForeignKey(CommunicationMethod, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return f"{self.company.name} - {self.method.name} ({self.date})"
