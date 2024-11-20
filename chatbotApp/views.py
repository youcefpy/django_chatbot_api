from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .nlp import get_response



class ChatBotView(APIView):
    def post(self,request):
        user_message = request.data.get("message",)

        if not user_message: 
            return Response({"error": "Message is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        #obtenir une reponse du model nlp 
        bot_response =  get_response(user_message)

        return Response({"response":bot_response},status=status.HTTP_201_CREATED)