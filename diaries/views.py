from .models import Diary, Comment
from .serializers import DiarySerializer, CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests #AI 챗봇 API 호출을 위한 requests 라이브러리리


# Create your views here.


#다이어리 상세 조회 (comment 보이게게)
@api_view(['GET'])
def diary_detail(request, diary_id):
    try:
        # 다이어리 ID와 사용자의 일치 확인(즉 해당 사용자의 다이어리만 조회)
        diary = Diary.objects.get(pk=diary_id, user=request.user) # 다이어리 id로 조회
    except Diary.DoesNotExist: # 다이어리가 없을 경우
        return Response({"error": "다이어리를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND) # 오류 반환




    # 다이어리 직렬화
    diary_serializer = DiarySerializer(diary)

    # 다이어리와 연결된 댓글을 찾고 링크 생성
    try:
        comment = Comment.objects.get(diary=diary)
    except Comment.DoesNotExist:
        comment = None

    # 댓글 링크 (없으면 None으로 표시)
    chatbot_url = None
    if comment:
        chatbot_url = f"/api/chatbot/ai/comment?year={diary.select_date.year}&month={diary.select_date.month}&day={diary.select_date.day}"

    return Response({
        "diary" : diary_serializer.data,
        "chatbot_url" : comment_serializer.data['chatbot_url']
    }, status=status.HTTP_200_OK) # 직렬화된 데이터 반환, 챗봇 url 포함함


# 다이어리 작성
@api_view(['POST'])
def diary_create(request): 
    serializer = DiarySerializer(data=request.data) # 다이어리 생성을 위한 직렬화
    if serializer.is_valid(): # 직렬화된 데이터가 유효한지 확인
        # 다이어리 저장 시 현재 사용자 정보와 연결결
        serializer.save(user = request.user) # 저장
        return Response(serializer.data, status=status.HTTP_201_CREATED) # 저장된 데이터 반환
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 오류 발생시 오류 반환










# 다이어리 수정
@api_view(['PUT'])
def diary_update(request, diary_id):
    try:
        diary = Diary.objects.get(pk=diary_id, user=request.user)  # 사용자별로 다이어리 조회
    except Diary.DoesNotExist:
        return Response({"error": "다이어리를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
    #다이어리 수정정
    serializer = DiarySerializer(diary, data=request.data)
    if serializer.is_valid():
        serializer.save()  # 다이어리 수정
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)