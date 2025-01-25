# 베이스 이미지
FROM python:3.9-slim

# 시간대 설정
ENV TZ=Asia/Seoul
RUN apt-get update && \
    apt-get install -y tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

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
