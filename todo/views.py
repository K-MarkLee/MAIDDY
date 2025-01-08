# from django.shortcuts import render ?????

from .models import Todo
from datetime import datetime
from rest_framework import status
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# To-do list 할일 표시
@api_view(['GET'])
def todo_list(request, date):
    date = request.query_params.get('date') # date를 query_params로 받아옴
    if not date:
        return Response({"error": "날짜가 필요합니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)     

    try:
        select_date = datetime.strptime(date, "%Y-%m-%d").date() # 날짜 형식 변환   
    except ValueError:
        return Response({"error": "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)
    
    todo = Todo.objects.filter(select_date=select_date, user=request.user).order_by("-created_at") # 사용자별로 할 일 조회
    serializer = TodoSerializer(todo, many=True) # 다수의 데이터 직렬화
    return Response(serializer.data, status=status.HTTP_200_OK)



# To-do list 생성 API
@api_view(['POST'])
def todo_create(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user) #현재 유저 정보에 To-do를 추가
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 작성 제거
@api_view(['DELETE'])
def todo_delete(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id, user=request.user) # 유저의 할 일만 삭제 가능하도록
    except Todo.DoesNotExist:
        return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)
    
    todo.delete()
    return Response({"message": "Todo list deleted successfully."}, status=status.HTTP_204_NO_CONETENT)



