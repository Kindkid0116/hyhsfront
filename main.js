async function submitStudent() {
  const name = document.getElementById("name").value;
  const num = document.getElementById("num").value;
  const userId = document.getElementById("user_id").value;

  if (!name || !num || !userId) {
      alert("모든 정보를 입력하세요.");
      return;
  }

  // 1️⃣ Flask로 학생 정보 저장 요청
  const response = await fetch("/submit", {
      method: "POST",
      headers: {
          "Content-Type": "application/json"
      },
      body: JSON.stringify({ name, num, user_id: userId })
  });

  if (response.ok) {
      // 2️⃣ JavaScript에서 카카오 메시지 전송
      sendKakaoMessage(userId);
      alert("등록 완료 및 카카오톡 알림 전송!");
  } else {
      alert("학생 등록에 실패했습니다.");
  }
}
