from .models import Todo
from rest_framework import status
from .serializers import TodoSerializer, CheckListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime


# To-do list 할일 표시
@api_view(['GET'])
def todo_list(request, date): # 달력으로 인해 특정 날짜에 관해서 todo 리스트 가져오기
    try:
        # 날짜 형식 검증
        selected_date = datetime.strptime(date, "%Y-%m-%d").date()

    except ValueError:
        return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

    # 해당 날짜에 해당하는 To-do 필터링
    todo = Todo.objects.filter(user=request.user, select_date=selected_date).order_by('-created_at')

    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



# 할 일 생성
@api_view(['POST'])
def todo_create(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user) #현재 유저 정보에 todo를 추가
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 할 일 수정/삭제
@api_view(['PUT','DELETE'])
def todo_update(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id, user=request.user) # 우저의 할 일만 수정 가능하게
    except Todo.DoesNotExist:
        return Response({"error": "Todo를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'DELETE':
        todo.delete()
        return Response({"message": "Todo를 성공적으로 삭제했습니다."}, status=status.HTTP_200_OK)

