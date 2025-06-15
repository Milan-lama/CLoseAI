from django.urls import path
from . import views

urlpatterns = [
    path('prompts/', views.generate_prompt, name='generate_prompt'),
]