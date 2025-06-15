from django.shortcuts import render
from .models import Prompt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializer import PromptSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_prompt(request):
    serializer = PromptSerializer(data=request.data)
    
    if serializer.is_valid():
        response_text = "do yourself i am not your slave its not 80s"
        
        prompt = Prompt.objects.create(
            user=request.user,
            propmt=serializer.validated_data['propmt'],
            propmt_answer=response_text,
            model='mock-model'
        )
        
        return Response(PromptSerializer(prompt).data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)