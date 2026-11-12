from django.shortcuts import render
from security.services.gemini_service import generate_response
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(["GET"])
def health_check(request):
    return Response({
        "status": "success",
        "message": "AI Security Playground API is running"
    })
    
@api_view(["POST"])
def chat(request):

    user_message = request.data.get("message")

    if not user_message:
        return Response({
            "error": "Message is required"
        }, status=400)

    ai_response = generate_response(user_message)

    return Response({
        "user_message": user_message,
        "ai_response": ai_response
    })
