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

### join.html

### main.html

```
method:'POST'
header : Content-Type: application/json
body : JSON.stringify
```

## Reference
```
자바스크립트의 fetch() 함수로 원격 API 호출하기(https://www.daleseo.com/js-window-fetch/)
API 설계 시 데이터 타입 POST, GET 사용법(https://as-j.tistory.com/43)
[CSS] 🎨 버튼(Button) 디자인 스타일 모음(https://inpa.tistory.com/entry/CSS-%F0%9F%92%8D-%EB%B2%84%ED%8A%BC-%EB%94%94%EC%9E%90%EC%9D%B8-%EB%AA%A8%EC%9D%8C)
```
