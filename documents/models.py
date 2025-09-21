from django.db import models
#from ..users.models import CustomUser
from django.contrib.auth.models import User

class Document(models.Model):
    file=models.FileField(upload_to="documents/")
    uploaded_by=models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(
        max_length=225,
        choices=[("pending", "POending"), ("processing", "Processing"), ("successful", "Successful")]
    )

class ExtractedField(models.Model):
    document=models.ForeignKey(Document, on_delete=models.CASCADE)
    field_name=models.CharField(max_length=225)
    field_value=models.TextField()
    confidence_score=models.FloatField()
