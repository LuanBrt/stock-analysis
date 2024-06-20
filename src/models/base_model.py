from django.db import models
import uuid

# Classe base abstrata que fornece campos comuns para outras modelos.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    
    class Meta:
        abstract = True
