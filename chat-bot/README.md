# OpenAI를 활용한 메뉴 추천 챗봇(오메추 BOT)
### 2023.09.05

## 목차
```
1. 개요
2. 기능 요구 사항
3. 기술 스택
4. 마감 기한
5. 테스트
6. 참고문서
```

## 개요
### 프로토타입
![chatbot  Untitled](https://github.com/onehowon/ormi3/assets/81984723/d1419fd5-e7c1-4d1a-ad13-3588b66a9ef6)

#### 오늘 뭐먹어야 할까? 고민하지 않고 AI에게 카테고리별로 추천 받을 수 있는 챗봇

## Requirement
### Feature
```
웹 기반 ChatBot 형태 서비스로 API 동작 하에 실시간으로 질문을 하여 입력값을 주면 AI가 상황에 맞는 답변인 결과값을 줌
AI는 메뉴 추천에 전문화 되었음을 인지하고 있어 "오늘 뭐먹지"라는 질문을 던지면, 카테고리 별(ex. 양식 / 중식 / 한식)로 세분화 이후 상황에 맞게 메뉴를 추천해줌
다이어트 중이거나 채식주의 등의 유저의 식습관에 따라서도 적절하게 상황을 인지함
```

## 개발환경
#### IDE : Visual Studio Code
#### Langauge : HTML, JS, CSS


## DeadLine
```
4 DAYS
```

## Test
### login.html
![login](https://github.com/onehowon/ormi3/assets/81984723/b2f2e756-5704-4ddf-8be1-9cf0748f014f)
```
메인화면으로, 제일 먼저 연결되는 page
① 사용자의 입력 부분 아이디와 비밀번호를 입력하는 border-box
② - 1) 아이디저장은 쿠키 값 세팅, 쿠키 값 삭제, 쿠키값 get 함수 생성
  - id 저장 체크 박스 기능 추가 후 그 전에 사용했던 id를 저장하여 처음 페이지 로딩
  - ID 저장하기를 체크 상태로 두도록 구현
  - 체크박스 변화 발생시(ID 저장하기 체크시) 쿠키 보관, ID 젖아하기 체크 해제 시 쿠키 삭제
  - ID 저장하기 체크한 상태에서 ID 입력시에도 쿠키 저장
  - 2) 자동 로그인
  - local storage에 저장된 사용자 정보 가져오도록 구현
  - 자동 로그인 체크했을 경우, 저장된 사용자 정보(ID/PW) 입력란에 자동으로 채움
  - 자동 로그인 시도
  - 원래는 회원 DB 연결하여 사용자 정보를 저장하여 받아와야 하지만, 아무 사용자나 성공한 것으로 간주
  - 로그인 성공 시, 자동로그인 정보 저장
③ 클릭시 main.html로 리다이렉션
④ 클릭시 join.html로 리다이렉션
```
### join.html
![join](https://github.com/onehowon/ormi3/assets/81984723/a26297aa-609f-423f-b315-500be358c9e9)
```
① 사용자의 입력 부분 아이디와 비밀번호, 비밀번호 확인을 입력하는 부분
② 이전 화면인 login.html로 리다이렉션
③ 계정 생성
  - onclick() 으로 동작
  - 공백으로 입력 되어 있을 경우 alert 화면 표출(필수 정보 입력 필요)
  - 비밀번호와 비밀번호 확인 value가 다른 경우 alert 표출(항목 일치X)
  - 비밀번호와 비밀번호 확인 value 일치시 alret 표출 및 login.html로 리다이렉션(회원가입 성공)
```
### main.html
![main](https://github.com/onehowon/ormi3/assets/81984723/6c7a7dc1-57b1-4aa1-a835-ab77ec070b3a)

```
method:'POST'
header : Content-Type: application/json
body : JSON.stringify
```

## Reference
```
COOKIE(쿠키)에 ID 값 저장하기. ID 저장 체크박스 만들기.(https://jy-note.tistory.com/22)
[자동로그인]session&cookie 활용 자동로그인 구현 예제 로직 및 과정(https://u-it.tistory.com/77)
```
