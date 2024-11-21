from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .nlp import get_response
import json
import logging

logger = logging.getLogger(__name__)

class ChatBotView(APIView):
    def post(self,request):
        try:
            # Ensure `message` is retrieved from JSON payload
            user_message = request.data.get("message", None)

            if not user_message:
                return Response({"error": "Message is required."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Get a response from the model
            bot_response = get_response(user_message)

            return Response({"response": bot_response}, status=status.HTTP_200_OK)

        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON payload."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)