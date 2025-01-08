# from django.shortcuts import render ?????

from .models import Todo
from .serializers import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# To-do list 할일 표시
@api_view(['GET'])
def todo_list(request):
    select_date = request.query_params.get('select_date')  # 쿼리 파라미터로 날짜 필터링
    if select_date:
        todo = Todo.objects.filter(user=request.user, select_date=select_date).order_by('-created_at')
    else:
        todo = Todo.objects.filter(user=request.user).order_by('-created_at')

    serializer = TodoSerializer(todo, many=True)
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



