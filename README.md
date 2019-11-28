# 종합프로젝트

### 0. 프로젝트 소개

- Django Web-Framework와 Vanila JS를 사용한 영화 추천 사이트
  - 선호장르 영화 추천 기능
  - 좋아요한 영화 관련 영화 추천 기능

## 1. Team

### 1-1 Team 정보

- 팀장 : 고병권
- 팀원 : 우동균
- 팀명 : 알보동

### 1-2 업무 분담

- 고병권
  1. Django accounts app MTV 제작.
  2. social login (kakao, google)
  3. 유저의 선호 장르가 포함된 영화 추천 기능 제작.
  4. 댓글 수정, 생성 기능 구현. (JavaScript 활용.)
  5. 선호 장르페이지 CSS 추가 .

- 우동균
  1. TMDb에서 받아온 영화 정보를 json파일로 제작.
  2. Django movies app MTV 기본 뼈대 제작.
  3. 좋아요한 영화와 비슷한 장르 영화 추천 기능 제작.
  4. 영화 세부정보 제작 및 UI  구성.
  5. Follow한 유저의 좋아요 한 영화 나열.
  6. 홈페이지 기본 UI 제작.

## 2. 목표 서비스 및 실제 구현 

### 2-1 목표 서비스

1. Social 로그인 기능
2. user 선호 장르를 통한 영화 추천 기능
3. 영화 세부정보 기능
4. 영화 좋아요 기능
5. 좋아요한 영화와 비슷한 영화 추천 기능
6. 영화의 댓글 기능
7. 유저들간의 Follow기능

### 2-2 실제 구현

#### 2-2-1 NOTION(개발 일지)

![](C:\Users\student\Desktop\project-img\notion1.JPG)

![](C:\Users\student\Desktop\project-img\notion2.JPG)

#### 2-2-2 프로젝트 구성 화면

- 로그인 화면

![](C:\Users\student\Desktop\project-img\login.JPG)

- 영화 추천 & 전체 영화

  - 영화 추천 

  ![](C:\Users\student\Desktop\project-img\m.JPG)

  - 전체 영화

  ![](C:\Users\student\Desktop\project-img\m2.JPG)

- 영화 세부사항

  - 기본구성

  ![](C:\Users\student\Desktop\project-img\d1.JPG)

  - 영화 트레일러 & 배우

  <img src="C:\Users\student\Desktop\project-img\d2.JPG" style="zoom: 67%;" />

  <img src="C:\Users\student\Desktop\project-img\d3.JPG" style="zoom: 67%;" />

  - 댓글(수정&삭제, follow 기능)

  ![](C:\Users\student\Desktop\project-img\d4.JPG)

- 사용자 정보

  - 기본 화면

  ![](C:\Users\student\Desktop\project-img\u1.JPG)

  - 선호 장르 수정

  ![](C:\Users\student\Desktop\project-img\u2.JPG)

  - 유저 비밀번호 변경

  ![](C:\Users\student\Desktop\project-img\u3.JPG)

## 3. 프로젝트 ERD

![](C:\Users\student\Desktop\project-img\snapshot.png)

## 4. 배포 서버 URL

- [http://movie-hospital.upuxkamv6m.ap-northeast-2.elasticbeanstalk.com](http://movie-hospital.upuxkamv6m.ap-northeast-2.elasticbeanstalk.com/)



## 5. 고찰

- 고병권
  - 유저가 원하는 장르의 추천영화목록을 출력. 원하는 장르가 없을 시 전체 추천영화목록(평점순)을 출력함. 시행착오 : 유저가 원하는 장르의 영화를 페이지에 띄우는 과정에서 django → html파일 → 파일 내 script로 전달하는 방법을 고려하였으나, 방법을 찾을 수가 없어 model에서 Genre ←→ User 간의 ManytoMany 구조를 추가하여 처리함.
  - 유저가 선택한 장르를 django로 넘기는 과정은 체크박스로 구현함. 시행착오 : 선택한 체크박스를 어떻게 django로 넘기면 좋을지 몰라 인터넷을 통해 검색.
  - 시행착오 : model form으로 전달 시 필수입력으로 평점을 입력해야 유효성 검사를 통과하는데, html파일에서 호출도 하지 않으면 값을 입력할 수 없었음. 호출해서 display:none 속성으로 평점만 감추고, 키 입력이나 마우스 입력시 변화된 값이 바로 반영되어 들어갈 수 있도록 함.
  - 오류처리 : 예고동영상을 실행 후 모달을 꺼도 실행이 유지되는 문제가 있었으나 인터넷 검색을 통해 해결

- 우동균
  - DB 제작에서 한 영화에 출연한 배우들의 DB를 만드는 과정에서 1:N 관계와 N:M관계의 개념이 정확하지 않아 여러번 models를 수정하는 시행착오를 했다. 여러번의 시행착오를 통해 각 영화에 5명의 배우들이 나오게 하고 영화와 배우의 사이에서 N:M 관계를 갖도록 제작했다.
  - 또한,  영화와 배우 사이의 관계에서 배우들의 정보를 제공하지 않아 에러가 발생 하는 경우가 생겼다. 이를 해결하기 위해 json 파일을 만드는 python 프로그램을 수정했다.
  - 유저가 좋아요한 영화들의 장르들을 뽑아내서 장르들이 포함된 다른 영화들을 추천하는 기능을 만들었다. 이 과정에서 model들간의 관계를 파악하고 query set들을 확인하며 기능을 추가하기 위해 노력했다.
  - 프로젝트의 UI를 구성하는데 있어 간결하게 만들기 위해서 노력했다.  이미 나와 있는 사이트들의 구성을 보면서 간결한 페이지를 찾기 위해 노력했고, Kakao page를 벤치마킹하여 제작 했다. 
  - 오류 처리 : 소셜 로그인 할 경우 직전에 로그아웃 했던 위치로 리다이렉트하는 문제가 있었으나 로그아웃 및 로그인 위치를 지정하여 해결