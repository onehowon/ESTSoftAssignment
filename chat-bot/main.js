
// DOM 요소
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
const chatContainer = document.querySelector('.wrap');

// "전송 버튼" 클릭 및 Enter 키 입력 처리
sendButton.addEventListener('click', handleSendMessage);
userInput.addEventListener('keydown', handleEnterKey);

async function handleSendMessage() {
    const userMessage = userInput.value.trim();

    if (userMessage.length === 0) {
        return; // 입력이 없는 경우 아무 동작도 하지 않음
    }

    // 메시지 추가
    addMessage('user', userMessage);

    // OpenAI API 호출 및 응답 처리
    await fetchAndAnswer(userMessage);

    // 사용자 입력창 초기화
    userInput.value = '';
}

function handleEnterKey(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); // 엔터 키의 기본 동작 막음
        handleSendMessage(); // "전송" 버튼 클릭과 동일한 동작 수행
    }
}

async function fetchAndAnswer(userMessage) {
    try {
        const url = 'https://estsoft-openai-api.jejucodingcamp.workers.dev/';

        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify([
                {"role": "system", "content": "assistant는 오늘 뭐먹을지 메뉴 추천해주는 전문가이다"},
                {"role": "user", "content": userMessage}
            ]),
        };

        const response = await fetch(url, requestOptions);

        if (!response.ok) {
            throw new Error('API 호출 중 에러 발생');
        }

        const responseData = await response.json();
        const answerText = responseData.choices[0].message.content;

        // 응답 메시지 추가
        addMessage('assistant', answerText);
    } catch (error) {
        console.error('API 호출 중 오류 발생', error);
    }
}

function addMessage(role, message) {
    const chatElement = document.createElement('div');
    chatElement.classList.add('chat', role === 'user' ? 'ch1' : 'ch2');

    const iconElement = document.createElement('div');
    iconElement.classList.add('icon');
    iconElement.innerHTML = '<i class="fa-solid fa-user"></i>';

    const textboxElement = document.createElement('div');
    textboxElement.classList.add('textbox');
    textboxElement.textContent = message;

    chatElement.appendChild(iconElement);
    chatElement.appendChild(textboxElement);

    chatContainer.appendChild(chatElement);
}
