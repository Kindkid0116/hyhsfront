Kakao.init("9b49aa02342896995714b81149a51bdc");  // 카카오 개발자 센터에서 발급한 JavaScript 키 입력
console.log("카카오 SDK 초기화 상태:", Kakao.isInitialized());


function loginWithKakao() {
    Kakao.Auth.authorize({
        redirectUri: "https://hyhsfront.onrender.com/auth/kakao/callback"
    });
}
// 카카오톡 메시지 보내기 함수
function sendKakaoMessage() {
    Kakao.API.request({
        url: "/v2/api/talk/memo/default/send",
        data: {
            template_object: {
                object_type: "text",
                text: "🚨 교복 위반 알림! 🚨\n\n학생이 교복 위반으로 등록되었습니다.",
                link: {
                    web_url: "https://hyhsfront.onrender.com",
                    mobile_web_url: "https://hyhsfront.onrender.com"
                }
            }
        },
        success: function(res) {
            console.log("메시지 전송 성공:", res);
            alert("카카오톡 메시지 전송 완료!");
        },
        fail: function(err) {
            console.error("메시지 전송 실패:", err);
            alert("카카오톡 메시지 전송 실패!");
        }
    });
}
