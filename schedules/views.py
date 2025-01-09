from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Schedule
from .serializers import ScheduleListSerializer, ScheduleDetailSerializer
from datetime import date # 날짜 픽스




# 일정표 표시
@api_view(['GET'])
def schedule_list(request):
    # 오늘 날짜의 시간표만 표시
    date = request.query_params.get('date')  # date를 query_params로 받아옴

    if not date:
        return Response({"error": "날짜가 필요합니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        select_date = datetime.strptime(date, "%Y-%m-%d").date()  # 날짜 형식 변환
    except ValueError:
        return Response({"error": "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)
    
    schedule = Schedule.objects.filter(select_date=select_date, user=request.user).order_by('time')  # 날짜 픽스, 오늘 날짜의 일정의의 시간순으로 정렬
    serializer = ScheduleListSerializer(schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



# 일정표 디테일
@api_view(['GET'])
def schedule_detail(request, schedule_id): # schedule_id와 user를 기준으로 일정 조회
    try:
        schedule = Schedule.objects.get(pk=schedule_id, user=request.user) 
    except Schedule.DoesNotExist:          
        return Response({"error": "해당 일정이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
    
    # 조회된 schedule을 serializer로 변환하여 반환
    serializer = ScheduleDetailSerializer(schedule)
    return Response(serializer.data, status=status.HTTP_200_OK)





# 일정표 작성
@api_view(['POST'])
def schedule_create(request):
    date = request.data.get('select_date')
    if not date:
        return Response({"error": "날짜가 필요합니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return Response({"error": "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = ScheduleDetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, select_date=date)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 일정표 수정
@api_view(['PUT'])
def schedule_update(request):
    schedule_id = request.query_params.get('id') # schedule_id를 query_params로 받아옴
    if not schedule_id:
        return Response({"error": "Schedule ID가 필요합니다."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        schedule = Schedule.objects.get(pk=schedule_id, user=request.user)
    except Schedule.DoesNotExist:
        return Response({"error": "해당 일정이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    serializer = ScheduleDetailSerializer(schedule, data=request.data, partial=True)
    

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# 일정표 삭제
@api_view(['DELETE'])
def schedule_delete(request, schedule_id):
    try:
        schedule = Schedule.objects.get(pk=schedule_id, user=request.user) # 유저의 일정표만 삭제 가능하도록
    except Schedule.DoesNotExist:
        return Response({"error": "schedule not found"}, status=status.HTTP_404_NOT_FOUND)
    
    schedule.delete()
    return Response({"message": "Schedule list deleted successfully."})





# 중요도 표시
@api_view(['PATCH'])
def schedule_pinned(request):
    date = request.query_params.get('date')
    schedule_id = request.query_params.get('id')

    if not date or not schedule_id:
        return Response({"error": "날짜와 일정 ID가 필요합니다."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        select_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return Response({"error": "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        schedule = Schedule.objects.get(pk=schedule_id, select_date = select_date, user=request.user)
    except Schedule.DoesNotExist:
        return Response({"error": "해당 일정이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    schedule.pinned = not schedule.pinned
    schedule.save()

    serializer = ScheduleDetailSerializer(schedule)
    return Response(serializer.data, status=status.HTTP_200_OK)
