from .models import Diary
from .serializers import DiarySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
# 다이어리 목록
@api_view(['GET'])
def diary_list(request): 
    diaries = Diary.objects.all().order_by('-select_date') # 최신순으로 정렬
    serializer = DiarySerializer(diaries, many=True) # 다이어리 목록을 직렬화
    return Response(serializer.data, status=status.HTTP_200_OK) # 직렬화된 데이터를 반환


# 다이어리 생성
@api_view(['POST'])
def diary_create(request): 
    serializer = DiarySerializer(data=request.data) # 다이어리 생성을 위한 직렬화
    if serializer.is_valid(): # 직렬화된 데이터가 유효한지 확인
        serializer.save(user = request.user) # 저장
        return Response(serializer.data, status=status.HTTP_201_CREATED) # 저장된 데이터 반환
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 오류 발생시 오류 반환


# 다이어리 상세 조회
@api_view(['GET'])
def diary_detail(request, diary_id):
    try:
        diary = Diary.objects.get(pk=diary_id) # 다이어리 id로 조회
    except Diary.DoesNotExist: # 다이어리가 없을 경우
        return Response({"error": "Diary not found"}, status=status.HTTP_404_NOT_FOUND) # 오류 반환
    
    if request.method == 'GET': # GET 요청인 경우
        serializer = DiarySerializer(diary) # 다이어리 직렬화
        return Response(serializer.data, status=status.HTTP_200_OK) # 직렬화된 데이터 반환
