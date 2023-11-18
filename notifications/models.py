from django.db import models
from django.utils import timezone

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=12, unique=True)
    operator_code = models.CharField(max_length=5)
    tag = models.CharField(max_length=255)
    timezone = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.phone_number} - {self.tag}"

class Dispatch(models.Model):
    id = models.AutoField(primary_key=True)
    start_datetime = models.DateTimeField(default=timezone.now)
    end_datetime = models.DateTimeField()
    message_text = models.TextField()
    client_filter_operator_code = models.CharField(max_length=5)
    client_filter_tag = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} - {self.start_datetime}"

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    creation_datetime = models.DateTimeField(null=True, default=timezone.now)
    status = models.CharField(max_length=255)
    dispatch = models.ForeignKey(Dispatch, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.creation_datetime} - {self.status}"
