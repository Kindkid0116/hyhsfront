Kakao.init("0b0a3dbfeff3a83de6ba52cc9e8c9922");  // 카카오 개발자 센터에서 발급한 JavaScript 키 입력
console.log("카카오 SDK 초기화 상태:", Kakao.isInitialized());

// 카카오 로그인 함수
function loginWithKakao() {
    Kakao.Auth.login({
        success: function(authObj) {
            console.log("로그인 성공:", authObj);
            alert("카카오 로그인 성공!");
        },
        fail: function(err) {
            console.error("로그인 실패:", err);
        }
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
                    web_url: "https://your-site.com",
                    mobile_web_url: "https://your-site.com"
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
