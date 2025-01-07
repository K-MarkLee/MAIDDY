from .models import Todo
from rest_framework import status
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# To-do list 할일 표시
@api_view(['GET'])
def todo_list(request):

    todo = Todo.objects.filter(user=request.user, select_date=select_date).order_by('-created_at')

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



# 작성 수정
@api_view(['PUT','DELETE'])
def todo_update(request, todo_id):
    if request.method == 'PUT':
        try:
            todo = Todo.objects.get(pk=todo_id, user = request.user) # 유저의 할 일만 수정 가능하도록
        except Todo.DoesNotExist:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == 'DELETE':
        try:
            todo = Todo.objects.get(pk=todo_id, user=request.user) # 유저의 할 일만 삭제 가능하도록
        except Todo.DoesNotExist:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)
        
        todo.delete()
        return Response({"message": "Todo list deleted successfully."}, status=status.HTTP_200_OK)

