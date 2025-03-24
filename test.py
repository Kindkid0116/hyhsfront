from flask import Flask, render_template, request, redirect, url_for
import database
import os


application = Flask(__name__, static_folder="static")
application.secret_key = "supersecretkey"

KAKAO_REST_API_KEY = os.getenv("0b0a3dbfeff3a83de6ba52cc9e8c9922")
KAKAO_REDIRECT_URI = "https://your-render-app.onrender.com/auth/kakao/callback"

@application.route('/auth/kakao/callback')
def kakao_callback():
    """카카오 로그인 콜백"""
    code = request.args.get("code")
    token_url = "https://kauth.kakao.com/oauth/token"
    
    data = {
        "grant_type": "authorization_code",
        "client_id": KAKAO_REST_API_KEY,
        "https://hyhsfront.onrender.com": KAKAO_REDIRECT_URI,
        "code": code
    }
    
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    res = requests.post(token_url, data=data, headers=headers)
    token_json = res.json()

    if "access_token" in token_json:
        session["kakao_token"] = token_json["access_token"]
        return redirect(url_for("index"))
    else:
        return "카카오 로그인 실패", 400
@application.route('/')
def index():
    return render_template('main.html')

@application.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    num = request.form['num']
    database.save(name, num)
    return render_template('index.html')

@application.route('/login')
def login():
    return render_template('login.html')
@application.route('/list')
def list():
    students = database.get_all_students()
    return render_template('list.html', stu=students)

@application.route('/password')
def password():
    return render_template('password.html')

@application.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    print(f"삭제 요청 ID: {id}")  # 디버깅
    database.delete_student(id)
    print("삭제 완료")
    return redirect(url_for('admit'))

@application.route('/admit')
def admit():
    """관리자 페이지"""
    students = database.get_all_students()  # 데이터베이스에서 학생 목록 가져오기
    print(f"현재 학생 목록: {students}")  # 디버깅용 출력
    return render_template('admit.html', stu=students)


@application.route('/passwordcheck', methods=['POST'])
def passwordcheck():
    password = request.form['pass']
    if password == "0102":
        return render_template('index.html')

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
