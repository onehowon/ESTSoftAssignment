const inputNews = document.getElementById('input-news');
const outputSummary = document.getElementById('output-summary');
const summarizeButton = document.getElementById('summarize-button');
const resetButton = document.getElementById('reset-button');

// 요약 버튼 클릭에 대한 이벤트 처리
summarizeButton.addEventListener('click', async () => {
  const newsText = inputNews.value.trim();
  if(newsText.length == 0){
    alert('뉴스 기사를 입력하세요');
    return;
  }

  // OpenAi API 호출해서 뉴스 기사 요약을 가져오는 로직 구현할 곳

  const summarizedText = await fetchAndSummarize(newsText);
  displaySummary(summarizedText);
});

resetButton.addEventListener('click', () => {
  inputNews.value = '';
  outputSummary.value = '';
});

// openai api 연동 및 요약 결과 가져오는 함수 구현 되야할 곳

async function fetchAndSummarize(newsText){

    try{

            // OpenAi API 엔드포인트 URL
    const url=`https://estsoft-openai-api.jejucodingcamp.workers.dev/`;

    // OpenAI API 호출 및 요약 결과 반환하는 코드 작성
    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`
        },
        body: JSON.stringify({
            model: "gpt-3.5-turbo",
            messages: [{
                role: "system",
                content: "assistant는 뉴스 기사 요약 전문가입니다."
            }, {
                role: "user",
                content: newsText // 수정된 부분: 변수 newsText를 사용하여 입력 내용을 전달
            }],
            temperature: 0.8,
            max_tokens: 1024,
            top_p: 1,
            frequency_penalty: 0.5,
            presence_penalty: 0.5,
            stop: ["Human"],
        }),
    };

    const response = await fetch(url, requestOptions);

    if(!response.ok){
        throw new Error('OpenAI API 호출 중 에러 발생');
    }

    const responseData = await response.json();
    const summarizedText = responseData.choices[0].message.content;
    return summarizedText;
    } catch(error){
        console.error('OpenAI API 호출 중 오류 발생', error);
        return '뉴스 기사 요약에 실패했습니다.'
    }
}

// 요약 결과 화면에 표시
function displaySummary(summaryText){
    outputSummary.value = summaryText;
}
