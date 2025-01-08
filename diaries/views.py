from rest_framework import status
from .models import Diary, Comment
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DiarySerializer, CommentSerializer


# 다이어리 상세 조회
@api_view(['GET'])
def diary_detail(request, date):
    try:
        # 다이어리 ID와 사용자의 일치 확인(즉 해당 사용자의 다이어리만 조회)
        diary = Diary.objects.get(select_date = date, user=request.user) # 다이어리 id로 조회
    except Diary.DoesNotExist: # 다이어리가 없을 경우
        return Response({"error": "다이어리를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND) # 오류 반환

    # 다이어리 직렬화
    diary_serializer = DiarySerializer(diary)

    # 다이어리와 연결된 코멘트을 찾고 링크 생성
    try:
        comment = Comment.objects.get(diary=diary)
        comment_serializer = CommentSerializer(comment)  # Comment 직렬화(1:1 관계라서, 맞나요?)

        chatbot_url = comment.chatbot_url
    except Comment.DoesNotExist:
        chatbot_url = None
        
    return Response({
        "diary" : diary_serializer.data,
        "chatbot_url" : chatbot_url, #프론트엔드에서 버튼 제공할 것
    }, status=status.HTTP_200_OK) # 직렬화된 데이터 반환, 챗봇 url 포함함



# 다이어리 작성 
@api_view(['POST'])
def diary_create(request): 
    serializer = DiarySerializer(data=request.data) # 다이어리 생성을 위한 직렬화
    if serializer.is_valid(): # 직렬화된 데이터가 유효한지 확인
        # 다이어리 저장 시 현재 사용자 정보와 연결
        diary = serializer.save(user = request.user) # 저장된 다이어리 객체를 diary 변수에 할당
        # 오류 방지를 위해 diary 다시 할당
        
        # Comment 생성 및 챗봇 URL 저장 #여기 아래에 api써야됨??
        chatbot_url = f"/api/chatbot/ai/comment?year={diary.select_date.year}&month={diary.select_date.month}&day={diary.select_date.day}/"
        Comment.objects.create(diary=diary, chatbot_url=chatbot_url) # Comment에 챗봇 url 저장
        
        return Response(serializer.data, status=status.HTTP_201_CREATED) # 저장된 데이터 반환
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 오류 발생시 오류 반환




# 다이어리 수정
@api_view(['PUT'])
def diary_update(request, diary_id):
    try:
        diary = Diary.objects.get(pk=diary_id, user=request.user)  # 사용자별로 다이어리 조회
    except Diary.DoesNotExist:
        return Response({"error": "다이어리를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
    #다이어리 수정
    serializer = DiarySerializer(diary, data=request.data)
    if serializer.is_valid():
        updated_diary = serializer.save()  # 다이어리 수정
        
        # 수정된 다이어리에 맞춰 챗봇 URL 갱신
        chatbot_url = f"/api/ai/chatbot/comment?year={updated_diary.select_date.year}&month={updated_diary.select_date.month}&day={updated_diary.select_date.day}"

        # 기존의 Comment가 있으면 URL 갱신, 없으면 새로 생성
        comment, created = Comment.objects.get_or_create(diary=updated_diary)
        comment.chatbot_url = chatbot_url
        comment.save()


        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 사용하는 이유는, 사용자가 chatbot_url(comment)을 클릭하여 챗봇 페이지로 이동할 때, 
# 쿼러미터에서 보다시피, URL에 포함된 year, month, day를 가져와 AI 챗봇 관련 페이지를 처리하는 역할을 하기에
# 사용한다.

# AI 챗봇 URL에 해당하는 페이지
@api_view(['GET'])
def comment_link(request):
    year = request.GET.get('year')
    month = request.GET.get('month')
    day = request.GET.get('day')

    # AI 코멘트 관련 로직 추가 가능
    return Response(
        {"message": f"Redirected to AI chatbot comment page for {year}-{month}-{day}"}
    )
