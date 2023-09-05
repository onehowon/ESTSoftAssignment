# OpenAI를 활용한 글 내용 정리 및 요약 봇
### 2023.09.04

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
### ![뉴스 요약봇  Untitled](https://github.com/onehowon/ToyProject/assets/81984723/94a8ed72-01d7-4483-86ec-e989f3d02cb1)
#### 뉴스 기사 원문을 복사하여 입력하면 사용자가 정독하기 편하도록 설계한 OpenAI 기반의 봇임
#### 디자이닝 없이 진행하는 프로젝트이기 때문에 디자인에 시간을 쏟기보다는, JS 기반의 기능을 구현하는데 더 초점을 두었음 카카오 오븐(kakao Oven)을 이용해 페이지 자체의 레이아웃만 잡았음

## Requirement
### Feature
```
웹 페이지의 형태의 서비스로 사용자가 입력(Input) 값인 글의 원문을 주면 API 기반의 AI가 결과(Output) 값인 요약문을 산출해내도록 함
기존에는 뉴스 기사 형식의 정형화된 게시글에 초점을 맞추었으나 다양한 형식의 글 또한 요약이 가능함
```

## 개발환경
#### IDE : Visual Studio Code
#### Langauge : HTML, JS, CSS


## DeadLine
```
HTML이나 CSS의 경우 레이아웃 구조 자체가 작성하는데 어렵지 않고, 디자인에 시간을 쏟지 않기로 했으므로 1일이면 충분하다고 판단하였음
API 및 모듈 호출, 입력 / 출력 등의 컨트롤러 구현 등에 더 초점이 잡혀진 JS에 더 시간을 소비해야 했기 때문에 2일~3일을 산정하여
총 4일의 DeadLine을 정하였음
+ 로컬로 진행하는 개인 프로젝트이므로 배포 단계는 생략하였음
```

## Test
### JS 주요 기능
### ![js기능](https://github.com/onehowon/ToyProject/assets/81984723/296af6b2-5e7a-4b17-8bf5-55b4d6b7eff4)
```
method:'POST'
header : Content-Type: application/json
body : JSON.stringify
```
### ![요약봇 2](https://github.com/onehowon/ToyProject/assets/81984723/11ee73e2-c2e9-4bfe-a48e-5344b6ce057b)
```
공백포함 2300자가 넘어가는 기존 뉴스의 글자 수를 241자까지 축소하여 요약해주고 있는 기능 구현 화면
```

## Reference
```
자바스크립트의 fetch() 함수로 원격 API 호출하기(https://www.daleseo.com/js-window-fetch/)
API 설계 시 데이터 타입 POST, GET 사용법(https://as-j.tistory.com/43)
[CSS] 🎨 버튼(Button) 디자인 스타일 모음(https://inpa.tistory.com/entry/CSS-%F0%9F%92%8D-%EB%B2%84%ED%8A%BC-%EB%94%94%EC%9E%90%EC%9D%B8-%EB%AA%A8%EC%9D%8C)
```
