from rest_framework import serializers
from .models import Prompt

class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ['id', 'propmt', 'propmt_answer', 'created_at', 'model']
        read_only_fields = ['propmt_answer', 'created_at', 'model']