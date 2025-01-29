from .models import Diary
from datetime import datetime
from rest_framework import status
from .serializers import DiarySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def diary_detail(request):
    date = request.query_params.get('date')
    if not date: 
        return Response({"error": "날짜가 필요합니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        select_date = datetime.strptime(date, "%Y-%m-%d").date()

    except ValueError:
        return Response({"error": "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        diary = Diary.objects.get(select_date = select_date, user=request.user) 
        serializer = DiarySerializer(diary) 
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    except Diary.DoesNotExist: 
        return Response({"error": "다이어리를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND) 


@api_view(['POST'])
def diary_update(request):
    date = request.data.get('select_date') 
    if not date: 
        return Response({"error": "날짜가 필요합니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        select_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return Response({"error": "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        diary = Diary.objects.get(select_date = select_date, user=request.user)  
        serializer = DiarySerializer(diary, data = request.data, partial=True) 
        if serializer.is_valid():
            update_diary = serializer.save() 
            return Response(DiarySerializer(update_diary).data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    except Diary.DoesNotExist: 

        serializer = DiarySerializer(data=request.data) 

        if serializer.is_valid(): 
            new_diary = serializer.save(user = request.user)
            return Response(DiarySerializer(new_diary).data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
