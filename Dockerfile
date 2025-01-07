# 베이스 이미지
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 종속성 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 앱 복사
COPY . .

EXPOSE 8000

# Django 앱 실행
CMD ["gunicorn", "maiddy.wsgi:application", "--bind", "0.0.0.0:8000"]
