function login(){
    var id = document.querySelector('#user-id');
    var pw = document.querySelector('#user-pw');

    // 공백일 경우 alret 발생, html에도 required로 필수 작성 칸으로 놔두긴 했음
    if(id.value == "" || pw.value == ""){
        alert("아이디와 비밀번호를 입력하세요!")
    }

    else{
        location.href = "main.html";
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
            alert("회원가입에 성공했습니다! 확인을 누르면 로그인 화면으로 이동합니다.")
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


// $(function(){
//     // id 저장 체크 박스 기능 추가
//     var userInputId = getCookie("userInputId");
//     $("manager_id").val(userInputId);

//     if($("#manager_id").val() != ""){ // 그 전에 id 저장해서 처음 페이지 로딩
//         $("#save-id").attr("checked", true); // ID 저장하기를 체크 상태로 두기
//     }

//     $("save-id").change(function(){ // 체크박스에 변화가 발생시
//         if($("#save-id").is(":chekced")){ // id 저장하기 체크했을 때
//             var userInputId = $("#manager_id").val();
//             setCookie("userInputId", userInputId, 7); // 7일간 쿠키 보관
//         } else{ // ID 저장하기 체크 해제 시
//             deleteCookie("userInputId");
//         }
//     });

//     // ID 저장하기 체크한 상태에서 id 입력시 이럴때도 쿠키 저장
//     $("#manager_id").keyup(function(){ // 입력 칸에 id를 입력시
//         if($("#useCookie").is("checked")){
//             var userInputId = $("#manager_id").val();
//             setCookie("userInputId", userInputId, 7);
//         }
//     });
// });

// // ID 저장하기 알고리즘 -->

// 자동 로그인 -->
window.onload = function(){
    const rememberMeCheckbox = document.getElementById('auto-login');
    const loginForm = document.querySelector('form');

    // 저장된 사용자 정보 가져오기
    const savedUsername = localStorage.getItem('username');
    const savedPassword = localStorage.getItem('password');
    const savedAutoLogin = localStorage.getItem('autoLogin');

    if(savedAutoLogin == 'true'){
        // 자동 로그인 체크 한 경우, 저장된 아이디 / 비밀번호 입력란에 채우기
        if(savedUsername && savedPassword){
            document.getElementById('user-id').value = savedUsername;
            document.getElementById('user-pw').value = savedPassword;
        }

        //로그인 시도
        login();
    }

    // 로그인 버튼 클릭 시 실행되는 함수
    function login(){
        const username = document.getElementById('user-id').value;
        const password = document.getElementById('user-pw').value;

        // 로그인 로직을 여기에 추가
        // 원래는 회원 DB 연결하여 사용자 정보를 받아와야 하나, 아무 사용자나 성공한 것으로 간주

        // 로그인 성공 시, 자동로그인 정보 저장
        if(rememberMeCheckbox.checked){
            localStorage.setItem('username', username);
            localStorage.setItem('password', password);
            localStorage.setItem('autoLogin', 'true');
        } else{
            localStorage.removeItem('username');
            localStorage.removeItem('password');
            localStorage.setItem('autoLogin', 'false');
        }

        // 실제 로그인 로직 추가할 부분
        // 로그인에 성공하면 다음 페이지로 리다이렉션 할 부분은 이미 login() 에 구현되어 있음
    }
};

function logout(){
    history.go(-1);
}