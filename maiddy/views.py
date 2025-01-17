from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

class ChatbotAPIView(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        query = request.data.get("query")
        
        try:
            ai_response = requests.post(
                'http://maiddy_ai:5000/chatbot/chatbot',
                
                json={
                    'user_id': user_id,
                    'query': query
                }
            )
            
            if ai_response.status_code == 200:
                return Response(ai_response.json(), status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": "AI 서버 응답 실패", "detail": ai_response.text}, 
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
                
        except requests.exceptions.RequestException as e:
            return Response(
                {"error": f"AI 서버 통신 오류: {str(e)}"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class FeedbackAPIView(APIView):
    def post(self, request):
        user_id = request.headers.get("user_id")
        select_date = request.data.get("select_date")
        
        try:
            ai_response = requests.post(
                'http://maiddy_ai:5000/feedback/',
                json={
                    'user_id': user_id,
                    'date': select_date  # AI 서비스는 'date'로 받고 있음
                }
            )
            
            if ai_response.status_code == 200:
                return Response(ai_response.json(), status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": "AI 서버 응답 실패", "detail": ai_response.text},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
                
        except requests.exceptions.RequestException as e:
            return Response(
                {"error": f"AI 서버 통신 오류: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class RecommendAPIView(APIView):
    def get(self, request):
        user_id = request.headers.get("user_id")
        
        try:
            ai_response = requests.get(
                'http://maiddy_ai:5000/recommend/',
                params={'user_id': user_id}
            )
            
            if ai_response.status_code == 200:
                return Response(ai_response.json(), status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": "AI 서버 응답 실패", "detail": ai_response.text},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
                
        except requests.exceptions.RequestException as e:
            return Response(
                {"error": f"AI 서버 통신 오류: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
