// 1번째 실습
// <!DOCTYPE html>
// <html lang="ko">
// <head>
//     <title></title>
// </head>
// <body>
//         <form action="./index.html" method="get">
//             id : <input name="id" type="text">
//             pw : <input name="pw" type="text">
//             <button type="submit">로그인</button>
//         </form> 
// </body>
// </html>


// 2번째 실습
let url = `https://estsoft-openai-api.jejucodingcamp.workers.dev/`;

let data = [{
    "role": "system",
    "content": "assistant는 제주 여행 전문가이다."
}]

data.push({
    "role": "user",
    "content": "주식회사 위니브에 대해 알려줘"
}, {
    "role": "assistant",
    "content": "주식회사 위니브는 제주에 있으며, 한국에서 가장많은 ICT 교육 콘텐츠를 보유한 회사입니다."
}, {
    "role": "user",
    "content": "주식회사 위니브에 대해 알려줘"
})

fetch(url, {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
    redirect: "follow",
})
    .then(res => res.json())
    .then(res => {
        console.log(res)
        console.log(res.choices[0].message.content)
    })

// 3번째 실습

let url = `https://estsoft-openai-api.jejucodingcamp.workers.dev/`;

let data= [{
    "role" : "system",
    "content": "assistant는 제주 여행 전문가이다."
}]

let data2 =[{
    "role" : "system",
    "content" : "assistant는 제주 여행 전문가이다."
}]

data.push({
    "role" : "user",
    "content" : "주식회사 위니브에 대해 알려줘"
},{
    "role" : "assistant",
    "cotnent": "주식회사 위니브는 제주에 있으며, 한국에서 가장많은 ICT 교육 콘텐츠를 보유한 회사입니다."
},{
    "role":"user",
    "content" : "주식회시 위니브에 대해 알려줘"
})

fetch(url, {
    method: "POST",
    headers:{
        "Content-Type": "appliaction/json",
    },
    body:JSON.stringify(data2),
    redirect: "follow",
})
    .then(res => res.json())
    .then(res =>{
        console.log(res)
        console.log(res.choices[0].message.content)
    })

    let url = `https://estsoft-openai-api.jejucodingcamp.workers.dev/`;

    let data = [{
        "role": "system",
        "content": "assistant는 제주 여행 전문가이다."
    }, {
        "role": "user",
        "content": "차가 없는 경우 제주 1박 2일 일정을 알려줘"
    }, {
        "role": "assistant",
        "content": "학습시키고 싶은 데이터 입력"
    }, {
        "role": "user",
        "content": "차가 없는 경우 제주 2박 3일 일정을 알려줘"
    }, {
        "role": "assistant",
        "content": "학습시키고 싶은 데이터 입력"
    }, {
        "role": "user",
        "content": "차가 있는 경우 제주 1박 2일 일정을 알려줘"
    }, {
        "role": "assistant",
        "content": "학습시키고 싶은 데이터 입력"
    }, {
        "role": "user",
        "content": "차가 있는 경우 제주 2박 3일 일정을 알려줘"
    }, {
        "role": "assistant",
        "content": "학습시키고 싶은 데이터 입력"
    }]
    
    data.push({
        "role": "user",
        "content": "차가 있는 경우 제주 2박 3일 일정을 알려줘"
    })
    
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data2),
        redirect: "follow",
    })
        .then(res => res.json())
        .then(res => {
            console.log(res)
            console.log(res.choices[0].message.content)
        })
    
    // 5번째 실습 => index.html에서 실습
    let url = `https://estsoft-openai-api.jejucodingcamp.workers.dev/`;
    
    let data = [{
        "role": "system",
        "content": "assistant는 제주 여행 전문가이다."
    }]
    
    data.push({
        "role": "user",
        "content": "차가 없는 경우 제주 1박 2일 일정을 알려줘"
    })
    
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data2),
        redirect: "follow",
    })
        .then(res => res.json())
        .then(res => {
            console.log(res)
            console.log(res.choices[0].message.content)
        })