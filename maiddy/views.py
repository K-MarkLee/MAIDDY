from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework.exceptions import PermissionDenied

class ChatbotAPIView(APIView):
    def post(self, request):
        # JWT 토큰에서 인증된 사용자 ID 가져오기
        authenticated_user_id = request.user.id
        requested_user_id = request.data.get("user_id")
        
        # 요청된 user_id와 인증된 사용자 ID 비교
        if str(authenticated_user_id) != str(requested_user_id):
            raise PermissionDenied("다른 사용자의 데이터에 접근할 수 없습니다.")
        
        query = request.data.get("query")
        
        try:
            ai_response = requests.post(
                'http://maiddy_ai:5000/chatbot/chat',
                headers={'user_id': str(authenticated_user_id)},  # 인증된 ID 사용
                json={
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
                
        authenticated_user_id = request.user.id
        requested_user_id = request.data.get("user_id")
        
        # 요청된 user_id와 인증된 사용자 ID 비교
        if str(authenticated_user_id) != str(requested_user_id):
            raise PermissionDenied("다른 사용자의 데이터에 접근할 수 없습니다.")
        
        select_date = request.data.get("select_date")
        
        try:
            ai_response = requests.post(
                'http://maiddy_ai:5000/feedback/',
                json={
                    'user_id': authenticated_user_id,
                    'select_date': select_date  # AI 서비스는 'date'로 받고 있음
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
    def post(self, request):
        authenticated_user_id = request.user.id
        requested_user_id = request.data.get("user_id")
        
        # 요청된 user_id와 인증된 사용자 ID 비교
        if str(authenticated_user_id) != str(requested_user_id):
            raise PermissionDenied("다른 사용자의 데이터에 접근할 수 없습니다.")
        
        
        try:
            ai_response = requests.get(
                'http://maiddy_ai:5000/recommend/',
                json={'user_id': authenticated_user_id}
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
