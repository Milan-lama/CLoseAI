from django.db import models
from django.contrib.auth.models import User

class Prompt(models.Model):
    propmt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    model = models.CharField(max_length=100, default='gpt-3.5-turbo')
    propmt_answer = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prompts')

