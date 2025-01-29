from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Schedule
from .serializers import ScheduleListSerializer, ScheduleDetailSerializer
from datetime import date 

@api_view(['GET'])
def schedule_list(request):
    date = request.query_params.get('date')

    if not date:
        return Response({"error": "날짜가 필요합니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        select_date = datetime.strptime(date, "%Y-%m-%d").date() 
    except ValueError:
        return Response({"error": "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 전달해주세요."}, status=status.HTTP_400_BAD_REQUEST)
    
    schedule = Schedule.objects.filter(select_date=select_date, user=request.user).order_by('time') 
    serializer = ScheduleListSerializer(schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def schedule_detail(request, schedule_id): 
    try:
        schedule = Schedule.objects.get(pk=schedule_id, user=request.user) 
    except Schedule.DoesNotExist:          
        return Response({"error": "해당 일정이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ScheduleDetailSerializer(schedule)
    return Response(serializer.data, status=status.HTTP_200_OK)

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


@api_view(['PUT'])
def schedule_update(request):
    schedule_id = request.query_params.get('id') 
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

@api_view(['DELETE'])
def schedule_delete(request, schedule_id):
    try:
        schedule = Schedule.objects.get(pk=schedule_id, user=request.user) 
    except Schedule.DoesNotExist:
        return Response({"error": "해당 일정을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
    
    schedule.delete()
    return Response({"message": "해당 일정을 성공적으로 삭제했습니다."})

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
