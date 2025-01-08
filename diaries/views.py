from .models import Diary
from datetime import datetime
from rest_framework import status
from .serializers import DiarySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# 다이어리 상세 조회
@api_view(['GET'])
def diary_detail(request):
    date = request.query_params.get('date')
    if not date: # 날짜가 없을 경우
        return Response({"error": "날짜가 필요합니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        select_date = datetime.strptime(date, "%Y-%m-%d").date() # 날짜 형식 변환
    except ValueError:
        return Response({"error": "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # 다이어리 ID와 사용자의 일치 확인(즉 해당 사용자의 다이어리만 조회)
        diary = Diary.objects.get(select_date = select_date, user=request.user) # 다이어리 id로 조회
        serializer = DiarySerializer(diary) # 직렬화
        return Response(serializer.data, status=status.HTTP_200_OK) # 직렬화된 데이터 반환
    
    except Diary.DoesNotExist: # 다이어리가 없을 경우
        return Response({"error": "다이어리를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND) # 오류 반환



# 다이어리 작성 
@api_view(['POST'])
def diary_update(request): # 생성 및 수정
    date = request.data.get('select_date') # 날짜를 받아옴
    if not date: # 날짜가 없을 경우
        return Response({"error": "날짜가 필요합니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        select_date = datetime.strptime(date, "%Y-%m-%d").date() # 날짜 형식 변환
    except ValueError:
        return Response({"error": "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)
    

    try:
        diary = Diary.objects.get(select_date = select_date, user=request.user)  # 사용자별로 다이어리 조회
        serializer = DiarySerializer(diary, data = request.data, partial=True) # 직렬화
        if serializer.is_valid():
            update_diary = serializer.save()  # 다이어리 수정
            return Response(DiarySerializer(update_diary).data, status=status.HTTP_200_OK) # 수정된 데이터 반환
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 오류 발생시 오류 반환

    except Diary.DoesNotExist: # 다이어리가 없을 경우

        serializer = DiarySerializer(data=request.data) # 다이어리 생성을 위한 직렬화

        if serializer.is_valid(): # 직렬화된 데이터가 유효한지 확인
            # 다이어리 저장 시 현재 사용자 정보와 연결
            new_diary = serializer.save(user = request.user)
            return Response(DiarySerializer(new_diary).data, status=status.HTTP_201_CREATED) # 저장된 데이터 반환
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 오류 발생시 오류 반환
