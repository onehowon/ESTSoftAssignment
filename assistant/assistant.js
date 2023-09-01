const fetch = require('node-fetch');

const apiUrl = 'https://apis.data.go.kr/B551011/DataLabService/metcoRegnVisitrDDList';
const apiKey = '8PW6wIE3abObBfc3DNhOOwyggfTPzrRVJjoC4k0cS4Du%2FaSkMLDjwKNJHOK%2F8oC7wz%2Brfe11mc8GrWgRGnNfwQ%3D%3D';

// API 요청 매개변수 설정
const params = new URLSearchParams({
  'numOfRows': 10,
  'pageNo': 10,
  'MobileOS': 'WIN',
  'MobileApp': 'Assistant',
  'serviceKey': apiKey,
  '_type': 'json',
  'startYmd': '2022-08-01',
  'endYmd': '2023-08-01',
  // 다른 매개변수 추가
});

// API 요청 URL 생성
const apiUrlWithParams = `${apiUrl}?${params.toString()}`;

// API 요청 보내기
fetch(apiUrlWithParams, {
  method: 'GET',
  headers: {
    'Accept': '*/*',
  },
})
  .then(response => response.json())
  .then(jsonData => {
    // JSON 형식으로 파싱된 데이터를 처리 (원하는 방식으로 파싱)
    console.log(jsonData);
    // 원하는 방식으로 데이터를 처리 및 표시
  })
  .catch(error => {
    console.error('JSON 형식 API 요청 실패:', error);
  });
