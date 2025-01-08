from .models import Todo
from datetime import datetime
from rest_framework import status
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# To-do list 할일 표시
@api_view(['GET'])
def todo_list(request):
    date = request.query_params.get('date') # date를 query_params로 받아옴
    is_completed = request.query_params.get('is_completed') # is_completed를 query_params로 받아옴
    

    if not date:
        return Response({"error": "날짜가 필요합니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)     
    try:
        select_date = datetime.strptime(date, "%Y-%m-%d").date() # 날짜 형식 변환   
    except ValueError:
        return Response({"error": "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)
    

    todo = Todo.objects.filter(select_date=select_date, user=request.user).order_by("-created_at") # 사용자별로 할 일 조회


    if is_completed is not None:
        todo = todo.filter(is_completed=(is_completed.lower() == 'true')) # is_completed가 True인 경우만 필터링
    

    serializer = TodoSerializer(todo, many=True) # 다수의 데이터 직렬화
    return Response(serializer.data, status=status.HTTP_200_OK)


  

# To-do list 완료 여부 변경
@api_view(['PATCH'])
def todo_checkbox(request): # 할 일 완료 여부 변경
    date = request.query_params.get('date') # date를 query_params로 받아옴
    todo_id = request.query_params.get('todo_id') # todo_id를 query_params로 받아옴

    if not date or not todo_id:
        return Response({"error": "날짜와 할 일 ID가 필요합니다."}, status=status.HTTP_400_BAD_REQUEST)
    

    try:
        select_date = datetime.strptime(date, "%Y-%m-%d").date() # 날짜 형식 변환
    except ValueError:
        return Response({"error": "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)
    

    try:
        todo = Todo.objects.get(pk=todo_id, select_date=select_date, user=request.user) # 할 일 ID로 조회
    except Todo.DoesNotExist:
        return Response({"error": "해당 조건에 맞는 todo를 찾을 수 없습니다. "}, status=status.HTTP_404_NOT_FOUND)
    


    todo.is_completed = not todo.is_completed # 할 일 완료 여부 변경
    todo.save() # 저장


    serializer = TodoSerializer(todo) # 직렬화
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
    return Response({"message": "Todo list deleted successfully."})



