function login(){
    var id = document.querySelector('#user-id');
    var pw = document.querySelector('#user-pw');

    // 공백일 경우 alret 발생, html에도 required로 필수 작성 칸으로 놔두긴 했음
    if(id.value == "" || pw.value == ""){
        alert("아이디와 비밀번호를 입력하세요!")
    }

    else{
        location.href = "index.html";
    }
}

function back(){
    history.go(-1);
}

function show(){
    var id = document.querySelector('#id');
    var pw = document.querySelector('#pw');
    var check_pw = document.querySelector('#check-pw');

    if(id.value == "" || pw.value == "" || check_pw.value == ""){
        alert("회원가입 하려면 필수항목을 모두 입력해주세요!")
    }
    else{
        if(pw.value == check_pw.value){
            location.href = 'login.html';
        }
        else{
            alert("비밀번호와 확인 항목이 일치하지 않습니다.");
        }
    }
}

// <-- ID 저장하기 알고리즘 

// 쿠키 값 세팅
function setCookie(cookieName, value, exdays){
    let exdate = new Date();
    exdate.setDate(exdate.getDate() + exdays);
    let cookieValue = escape(value) + ((exdays==null) ? "" : "; expires=" + exdate.toGMTString());
    document.cookie = cookieName + "=" + cookieValue;
}

// 쿠키 값 delete
function deleteCookie(cookieName){
    let expireDate = new Date();
    expireDate.setDate(expireDate.getDate() -1);
    document.cookie = cookieName + "=" + "; express=" + expireDate.toGMTString();
}

// 쿠키값 get
function getCookie(cookieName){
    cookieName = cookieName + "=";
    let cookieData = document.cookie;
    let start = cookieDate.indexOf(cookieName);
    let cookieValue ='';
    if(start != -1){
        start += cookieName.length;
        let end = cookieData.indexOf(';', start);
        if(end == -1)end = cookieData.length;
        cookieValue = cookieData.substring(start, end);
    }
    return unescape(cookieValue);
}

$(function(){
    // id 저장 체크 박스 기능 추가
    var userInputId = getCookie("userInputId");
    $("manager_id").val(userInputId);

    if($("#manager_id").val() != ""){ // 그 전에 id 저장해서 처음 페이지 로딩
        $("#save-id").attr("checked", true); // ID 저장하기를 체크 상태로 두기
    }

    $("save-id").change(function(){ // 체크박스에 변화가 발생시
        if($("#save-id").is(":chekced")){ // id 저장하기 체크했을 때
            var userInputId = $("#manager_id").val();
            setCookie("userInputId", userInputId, 7); // 7일간 쿠키 보관
        } else{ // ID 저장하기 체크 해제 시
            deleteCookie("userInputId");
        }
    });

    // ID 저장하기 체크한 상태에서 id 입력시 이럴때도 쿠키 저장
    $("#manager_id").keyup(function(){ // 입력 칸에 id를 입력시
        if($("#useCookie").is("checked")){
            var userInputId = $("#manager_id").val();
            setCookie("userInputId", userInputId, 7);
        }
    });
});

// ID 저장하기 알고리즘 -->