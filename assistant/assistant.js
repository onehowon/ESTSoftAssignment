const inputNews = document.getElementById('input-news');
const outputSummary = document.getElementById('output-summary');
const summarizeButton = document.getElementById('summarize-button');
const resetButton = document.getElementById('reset-button');

// openAI api 사용해서 뉴스 기사 요약 로직 구현할 곳

// 요약 결과 outputSummary에 표시할 함수

function displaySummary(summaryText){
  outputSummary.value = summaryText;
}

// 요약 버튼 클릭에 대한 이벤트 처리
summarizeButton.addEventListener('click', async () => {
  const newsText = inputNews.value.trim();
  if(newsText.length == 0){
    alert('뉴스 기사를 입력하세요');
    return;
  }

  // OpenAi API 호출해서 뉴스 기사 요약을 가져오는 로직 구현할 곳

  // 가져온 요약 결과는 displaySUmmary 함수 사용하여 출력
  const summarizedText = await fetchAndSummarize(newsText);
  displaySummary(summarizedText);
});

resetButton.addEventListener('click', () => {
  inputNews.value = '';
  outputSummary.value = '';
});

// openai api 연동 및 요약 결과 가져오는 함수 구현 되야할 곳
async function fetchAndSummarize(newsText){
  //openai api 호출 및 요약 결과를 반환하는 코드 작성
  // 반환된 요약 결과 리턴
  // 이 부분은 open ai api와의 통합에 필요한 코드로 대체 되어야함
  return '뉴스 기사 요약 결과입니다.';
}
