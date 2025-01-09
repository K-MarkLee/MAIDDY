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
    today_date = date.today()
    schedule = Schedule.objects.filter(select_date=today_date, user=request.user).order_by('time')  # 날짜 픽스, 오늘 날짜의 일정의의 시간순으로 정렬
    serializer = ScheduleListSerializer(schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 일정표 작성
@api_view(['POST'])
def schedule_create(request):
    request_data = request.data  # 직접 사용
    request_data['select_date'] = date.today()  # 고정된 날짜로 오늘 날짜 설정

    serializer = ScheduleDetailSerializer(data=request_data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 일정표 수정
@api_view(['PUT'])
def schedule_update(request):
    schedule_id = request.data.get('id')
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





# @api_view(['POST'])
# def schedule_update(request):
#     schedule_id = request.data.get('id')  # schedule id가 있어야 수정이 가능
#     serializer = ScheduleDetailSerializer(data=request.data)

#     if schedule_id:
#         # 수정 처리 (기존 일정 수정)
#         try:
#             schedule = Schedule.objects.get(pk=schedule_id, user=request.user)  # 유저의 일정만 수정 가능
#         except Schedule.DoesNotExist:  
#             return Response({"error": "해당 일정이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = ScheduleDetailSerializer(schedule, data=request.data, partial=True)  # 부분 수정 가능
#         if serializer.is_valid():
#             serializer.save()  # 변경 사항 저장
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     # 일정이 새로 생성되는 경우
#     request_data = request.data.copy()  # 요청 데이터를 복사
#     request_data['select_date'] = date.today()  # 고정된 날짜로 오늘 날짜를 설정

#     serializer = ScheduleDetailSerializer(data=request_data)
#     if serializer.is_valid():
#         serializer.save(user=request.user)  # 현재 유저 정보에 일정을 추가
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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
    schedule_id = request.data.get('id')
    pinned = request.data.get('pinned')

    if not schedule_id or pinned is None:
        return Response({"error": "Schedule ID와 pinned 값이 필요합니다."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        schedule = Schedule.objects.get(pk=schedule_id, user=request.user)
    except Schedule.DoesNotExist:
        return Response({"error": "해당 일정이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    schedule.pinned = pinned
    schedule.save()

    return Response(ScheduleDetailSerializer(schedule).data, status=status.HTTP_200_OK)
