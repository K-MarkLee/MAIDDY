## 📖 Navigation

1. [👀 Introduction](#introduction)
2. [🛠 Setup](#setup)
3. [👩🏻‍💻 Features](#features)
4. [📝 Techstack](#techstack)
5. [🌐 Architecture](#architecture)
6. [🗂 ERD](#erd)
7. [🎨 WIREFRAME](#wireframe)
8. [👨‍👩‍👧‍👦 Team](#team)

<br>

<a name="introduction"></a>
## 👀 Introduction
![Image](https://github.com/user-attachments/assets/d15ad40b-460d-452a-9d48-1ed9ab7cb8aa)

<br>

# MAIDDY: AI 기반 다이어리 및 스케줄러  
**My AI Daily Diary**
<br>
숏폼미디어으로 인해 짧아진 집중력과 복잡한 일상 속에서, MAIDDY는 단순한 일정 관리 도구를 넘어 개인화된 추천과 동기부여를 제공하는 "다이어리 메이트"입니다.  
사용자 데이터를 분석해 맞춤 일정을 제안하고 하루를 정리하며 목표 달성을 돕는 동반자로서, 중요한 일을 체계적으로 관리하고 삶의 질을 높이는 데 도움을 줍니다.  




### 🗓 Duration
| 날짜            | 업무                 |
|---------------|--------------------|
| 12.30 ~ 12.31 | 아이디어 회의 및 마인드맵      |
| 12.31 ~ 01.03 | 기능 명세서 작성 및 기능 설계   |
| 01.03 ~ 01.14 | MVP 개발 |
| 01.15 | 중간 발표 |
| 01.15 | 중간 점검 및 추가 기능 설계 |
| 01.16 ~ 01.22 | 추가기능 구현 및 서버 배포  |


<br>

<a name="setup"></a>
## 🛠 Setup 
To set up and run the project, follow these steps:

1. Clone the project repository:

    ```bash

    ```

2. Navigate to the project directory:

    ```bash
 
    ```

3. **Install the required dependencies:**

    ```bash
  
    ```

4. **Create and configure the `config.py` file:**

    Create a file named `config.py` in the project root directory and add the following content:

    ```python
    # config.py


    ```

5. **Apply database migrations:**

    ```bash
  
    ```

6. **Run the development server:**

    ```bash

    ```

7. **Open your browser and visit:**



<a name="features"></a>
## 👩🏻‍💻Features
### 스케쥴러 및 투두리스트
- **타임테이블 형식**: 시각적으로 일정을 한눈에 확인할 수 있는 타임테이블 제공
- **세부 일정 편집**: 추가 버튼과 탭 이동을 활용해 일정 세부사항 편집 가능
- **중요 일정 PIN 기능**: 우선순위 높은 일정을 메인 페이지에 고정하여 쉽게 확인
- **체크리스트 형식**: 간단하고 직관적인 체크리스트로 할 일 관리
- **리스트 편집**: 추가 및 삭제 버튼을 통해 TODO 리스트를 유연하게 구성 가능

<details>
<summary>미리보기</summary>
<div markdown="1">
    

 <br>
</div>
</details>

<br>

### 다이어리 및 AI코멘트
- **쉬운 접근성**: 메인 페이지의 캘린더와 네비게이션 바를 통해 일기 페이지에 손쉽게 접근 가능
- **텍스트 형식 기록**: 하루를 간단히 기록하고 돌아볼 수 있도록 텍스트 형식으로 일기 저장
- **AI 코멘트 기능**: 코멘트 버튼을 통해 AI가 TODO 리스트와 일기 내용을 분석하여 하루를 평가하는 코멘트 제공

<details>
<summary>미리보기</summary>
<div markdown="1">


 <br>
</div>
</details>

<br>

### AI 기반 개인화 서비스
- **AI 코멘트 제공**: 사용자의 데이터를 분석하여 하루를 돌아보고 개선 방향을 제시
- **개인화된 챗봇**: 사용자와 자연스럽게 소통하며 개인 맞춤형 경험 제공
- **일정 및 리스트 추천**: 데이터를 바탕으로 일정과 리스트를 추천하고, 반복 행동을 학습해 루틴화 지원
- **데이터 기반 학습**: 스케줄러를 통해 사용자 데이터를 주기적으로 학습, 개인화 서비스 지속 제공


<details>
<summary>미리보기</summary>
<div markdown="1">


 <br>
</div>
</details>

<br>

<a name="techstack"></a>
## 📝 Technologies & Tools
<div align=center><h1>📚 STACKS</h1></div>

<div align=center> 
  <!-- Frontend -->
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white"> 
  <img src="https://img.shields.io/badge/Tailwind%20CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white">
  <br>
  
  <!-- Backend -->
  <img src="https://img.shields.io/badge/Django%20DRF-092E20?style=for-the-badge&logo=django&logoColor=white"> 
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white">
  <br>
  
  <!-- AI -->
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white"> 
  <img src="https://img.shields.io/badge/FAISS-0086FF?style=for-the-badge&logo=faiss&logoColor=white">
  <img src="https://img.shields.io/badge/Embeddings-3A86FF?style=for-the-badge&logo=ai&logoColor=white">
  <br>
  
  <!-- Database -->
  <img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white"> 
  <br>
  
  <!-- Cloud/Infrastructure -->
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white"> 
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
  <img src="https://img.shields.io/badge/Python%203.9-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <br>
  
  <!-- Collaboration -->
  <img src="https://img.shields.io/badge/JIRA-0052CC?style=for-the-badge&logo=jira&logoColor=white"> 
  <img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white">
  <img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white">
  <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white">
</div>

<br>

<a name="architecture"></a>
## 🌐 Architecture
![Image](https://github.com/user-attachments/assets/4b57876a-6f81-49a9-a639-11c70f576bcd)

<br>

<a name="erd"></a>
## 🗂 ERD
![Image](https://github.com/user-attachments/assets/eae194e1-8c5e-490d-9432-dd7ea0ce542b)

<br><br>



<a name="wireframe"></a>
## 🎨 WIREFRAME
![Image](https://github.com/user-attachments/assets/9fd46de8-d1c6-4dfd-b6fe-75498c436665)

<br><br>


<a name="team"></a>
## 👨‍👩‍👧‍👦 Team
![Image](https://github.com/user-attachments/assets/68f62f85-021f-46b9-8504-12db66832ee8)


#### [📝 SA 문서 바로가기] (https://www.notion.so/teamsparta/Young-POTY-SA-636a5824bd96466bafb740b6b1cf9ff7)
#### [👊 팀 노션 바로가기] (https://www.notion.so/teamsparta/Young-POTY-16c2dc3ef514818982acc5fa7fdc4f07)
#### [🌟 프로젝트 브로셔 보러가기]
#### [🤖 AI REPOSITORY] (https://github.com/K-MarkLee/MAIDDY_AI)
#### [🖥️ FRONT REPOSITORY]
