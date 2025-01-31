## 🧷 Other Repo
#### [🤖 AI REPOSITORY] (https://github.com/K-MarkLee/MAIDDY_AI)
#### [🖥️ FRONT REPOSITORY] (https://github.com/K-MarkLee/MAIDDY_Front)
<br>


## 📖 Navigation

1. [👀 Introduction](#introduction)
2. [🛠 Setup](#setup)
3. [👩🏻‍💻 Features](#features)
4. [📝 Techstack](#techstack)
5. [🌐 Architecture](#architecture)
6. [🗂 ERD](#erd)
7. [🎨 Wireframe](#wireframe)
8. [📜Sequence Diagram](#sequencediagram)
9. [👨‍👩‍👧‍👦 Team](#team)

<br>

## ✒️ Sites
#### [📝 SA Documents] (https://www.notion.so/teamsparta/Young-POTY-SA-1882dc3ef51480cb8187c9e556dc24a6)
#### [👊 Team Notion] (https://www.notion.so/teamsparta/Young-POTY-16c2dc3ef514818982acc5fa7fdc4f07)
#### [🌟 Project Brochure] (https://teamsparta.notion.site/AI-8-1702dc3ef514803cbc3ef17621bcaa08?p=1702dc3ef514807fa915e4fe04cd99ba&pm=c)

<br>

---
<a name="introduction"></a>
## 1. 👀 Introduction
![Image](https://github.com/user-attachments/assets/d15ad40b-460d-452a-9d48-1ed9ab7cb8aa)

<br>

## MAIDDY (My AI Daily Diary)
### AI 기능이 탑재된 스케줄러 & 다이어리 혼합 플랫폼

<br>
요즘 유행하는 숏폼(Short-form) 콘텐츠의 확산은 사람들의 집중력 저하와 얕은 사고를 초래하며,<br>
이는 일정 관리와 목표 달성에 어려움을 주고 있습니다. 이를 해결하기 위해, AI를 활용한 직관적이고 효율적인 도구를 개발하고 있습니다.<br>
단순한 일정 관리 도구를 넘어, 개인 맞춤형 일정 추천과 동기부여 피드백을 통해 사용자가 시간을 효율적으로 관리하고,<br>
목표에 집중할 수 있도록 도와주는 동반자로서, 다이어리 메이트인 My AI Daily Diary, MAIDDY를 소개합니다.<br>
<br>

- 핵심 목표: 사용자에게 효율적인 일정 관리 및 목표 달성 지원<br>
- 해결하려는 문제: 사용자의 집중력 저하와 얕은 사고로 인한 목표 달성의 어려움



### 🗓 Duration
| 날짜            | 업무                 |
|---------------|--------------------|
| 12.30 ~ 12.31 | 아이디어 회의 및 마인드맵      |
| 12.31 ~ 01.03 | 기능 명세서 작성 및 기능 설계   |
| 01.03 ~ 01.14 | MVP 개발 |
| 01.15 | 중간 발표 |
| 01.15 | 중간 점검 및 추가 기능 설계 |
| 01.16 ~ 01.22 | 추가기능 구현 및 서버 배포  |
| 01.23 ~ 01.27 | 유저테스트 및 결과를 바탕으로 분석 |
| 01.28 ~ 01.30 | 유저테스트 바탕으로 기능 보완 및 전반적인 내용 정리 |

<br>

---

<a name="setup"></a>
## 2. 🛠 Setup  (프로젝트 설치 및 실행 방법, 필요한 환경 설정 등 작성 부탁)
AI set up is on AI repository

  
To set up and run the project, follow these steps:

### Frontend

1. Clone the project repository:

    ```
    https://github.com/K-MarkLee/MAIDDY_Front/
    ```

2. Navigate to the project directory:

    ```
    cd MAIDDY_Front/frontend/my-diary-app
    ```

3. **Create `.env` file:**

    Create a file named `config.py` in the project root directory and add the following content:

    ```
    NEXT_PUBLIC_API_URL, NEXT_PUBLIC_FRONTEND_URL
    ```

4. **Run the docker:**

    ```
    docker-compose up --build
    ```

---
### Backend

1. Clone the project repository:
    ```
    https://github.com/K-MarkLee/MAIDDY/
    ```

2. Navigate to the projec directory:
    ```
    cd MAIDDY
    ```
    
3. **Create `.env` file:**
    Create a file named `.env` in the project root directory and add the following content:
    ```
    DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DATABASE_URL, FRONTENT_IP, BACKEND_IP
    ```

4. **Run the docker:**
    ```
    docker-compose up --build
    ```



5. Apply database migration
    ```
    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate
    ```
    
6. Connect to address
    ```
    maiddy.co.kr/
    ```


<a name="features"></a>

---


## 3. 👩🏻‍💻Features
### 📅 달력 및 일정과 할일
- **달력 형식**: 시각적으로 일정을 한눈에 확인 가능
- **세부 일정 편집**: 일정 추가 및 탭 이동으로 세부 사항 수정
- **중요 일정을 달력 위에 고정 기능**: 우선순위 높은 일정을 메인 페이지에 고정하여 빠르게 확인 가능
- **체크리스트 형식**: 간단한 체크리스트로 할 일 관리
- **할일 목록 편집**: 할일 목록을 유연하게 추가/삭제 가능

<br>

### 📖 다이어리 및 AI코멘트
- **쉬운 접근성**: 달력과 네비게이션 바를 통해 바로 일기 페이지 빠르게 접근
- **텍스트 형식 기록**: 하루를 간단히 기록하고 되돌아보기
- **AI 코멘트**: 코멘트 버튼을 통해 AI가 오늘 일정, 할일 리스트 및 일기 내용을 분석 후 하루 평가 및 개선 제시

<br>

### 🤖AI 기반 개인화 서비스
- **AI 코멘트**: 사용자의 데이터를 분석하여 하루를 돌아보고 개선 방향 제시
- **개인화된 챗봇**: 사용자와 자연스럽게 소통하며 개인 맞춤형 경험 제공
- **일정 및 할일 추천**: 데이터를 바탕으로 일정과 리스트를 추천
- **데이터 기반 학습**: 스케줄러를 통해 사용자 데이터를 주기적으로 학습, 개인화 서비스 지속 제공
<br>

---
<a name="techstack"></a>
## 4. 📝 Techstack

 ### 프론트엔드 (Frontend)
-  **Next.js**: React 기반의 서버사이드 렌더링 및 정적 웹 애플리케이션 개발
- **Tailwind CSS**: 유틸리티 중심의 CSS 프레임워크로 빠른 UI 개발 가능
- **shadcn/ui**: UI 구성 요소 라이브러리로 일관성 있는 디자인 제공

### 백엔드 (Backend)
- **Django**: 강력한 웹 프레임워크로 효율적인 백엔드 개발
- **Django REST Framework (DRF)**: RESTful API 설계 및 구현
- **JWT (JSON Web Token)**: 인증 및 보안 토큰 관리

 ### AI 서비스 (AI Services)
- **OpenAI**: 자연어 처리 기반의 AI 모델 활용
- **LangChain**: AI 응답 체계 및 워크플로우 설계
- **pgvector**: PostgreSQL에서 벡터 데이터를 효율적으로 관리 및 검색
- **Flask**: 간결하고 가벼운 웹 프레임워크로 AI 서비스 통합

 ### 데이터베이스 (Database)
- **PostgreSQL**: 안정성과 확장성을 갖춘 관계형 데이터베이스
- **pgvector**: AI 임베딩 데이터 관리를 위한 PostgreSQL 확장

 ### 클라우드 및 인프라 (Cloud/Infrastructure)
- **AWS EC2**: 서버 호스팅 및 애플리케이션 실행
- **Docker**: 컨테이너 기반 개발 및 배포
- **Nginx**: 리버스 프록시 및 서버 관리
- **Gunicorn**: Python WSGI 서버로 안정적인 애플리케이션 실행

 ### 협업 도구 (Collaboration)
- **JIRA**: 프로젝트 관리 및 이슈 트래킹
- **Figma**: UI/UX 디자인 협업 도구
- **Slack**: 팀 커뮤니케이션 및 알림 관리
- **Notion**: 문서화 및 작업 관리

<div align="center">
  <!-- Frontend -->
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white">
  <img src="https://img.shields.io/badge/Tailwind%20CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white">
  <img src="https://img.shields.io/badge/shadcn/ui-000000?style=for-the-badge&logo=shadcn/ui&logoColor=white">
  <br>
  <!-- Backend -->
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/Django%20REST%20Framework-000000?style=for-the-badge&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=javascript&logoColor=white">
  <br>
  <!-- AI Services -->
  <img src="https://img.shields.io/badge/OpenAI-000000?style=for-the-badge&logo=openai&logoColor=white">
  <img src="https://img.shields.io/badge/LangChain-000000?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/pgvector-000000?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
  <br>
  <!-- Database -->
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/pgvector-000000?style=for-the-badge&logo=postgresql&logoColor=white">
  <br>
  <!-- Cloud/Infrastructure -->
  <img src="https://img.shields.io/badge/AWS%20EC2-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
  <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
  <img src="https://img.shields.io/badge/Gunicorn-000000?style=for-the-badge&logo=gunicorn&logoColor=white">
  <br>
  <!-- Collaboration -->
  <img src="https://img.shields.io/badge/JIRA-0052CC?style=for-the-badge&logo=jira&logoColor=white">
  <img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white">
  <img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white">
  <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white">
</div>


<br>

---
<a name="architecture"></a>
## 5.🌐 Architecture
![image](https://github.com/user-attachments/assets/33d9b8d4-fe1e-450f-b640-372e4e86a393)


<br>

---

<a name="erd"></a>
## 6. 🗂 ERD
![image](https://github.com/user-attachments/assets/b244d927-53dd-45b7-b341-42ae47062693)


<br><br>


---
<a name="wireframe"></a>
## 7. 🎨 Wireframe
![image](https://github.com/user-attachments/assets/a0b1ae7f-69f3-4780-9c90-4932aafe5c71)


<br><br>

---
<a name="sequencediagram"></a>
## 8. 📜 Sequence Diagram
![image](https://github.com/user-attachments/assets/3677b8e5-2c9e-4804-b16e-276d3147457a)


<br><br>

---
<a name="team"></a>
## 9. 👨‍👩‍👧‍👦 Team
![image](https://github.com/user-attachments/assets/46d5d456-7ddd-4e2e-940e-51cc1420a1b8)


