from .models import Diary
from .serializers import DiarySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
# 다이어리 목록
@api_view(['GET'])
def diary_list(request):
    diaries = Diary.objects.filter(user=request.user).order_by('-select_date')
    # 로그인한 사용자에 해당하는 다이어리만 조회, 최신순으로 정렬
    serializer = DiarySerializer(diaries, many=True) # 다이어리 목록을 직렬화
    return Response(serializer.data, status=status.HTTP_200_OK) # 직렬화된 데이터를 반환


# 다이어리 생성
@api_view(['POST'])
def diary_create(request): 
    serializer = DiarySerializer(data=request.data) # 다이어리 생성을 위한 직렬화
    if serializer.is_valid(): # 직렬화된 데이터가 유효한지 확인
        # 다이어리 저장 시 현재 사용자 정보와 연결결
        serializer.save(user = request.user) # 저장
        return Response(serializer.data, status=status.HTTP_201_CREATED) # 저장된 데이터 반환
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 오류 발생시 오류 반환


# 다이어리 상세 조회
@api_view(['GET'])
def diary_detail(request, diary_id):
    try:
        # 다이어리 ID와 사용자의 일치 확인(즉 해당 사용자의 다이어리만 조회)
        diary = Diary.objects.get(pk=diary_id, user=request.user) # 다이어리 id로 조회
    except Diary.DoesNotExist: # 다이어리가 없을 경우
        return Response({"error": "Diary not found"}, status=status.HTTP_404_NOT_FOUND) # 오류 반환
    
    if request.method == 'GET': # GET 요청인 경우
        serializer = DiarySerializer(diary) # 다이어리 직렬화
        return Response(serializer.data, status=status.HTTP_200_OK) # 직렬화된 데이터 반환
