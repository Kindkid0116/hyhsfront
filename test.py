from flask import Flask, render_template, request, redirect, url_for
import database
import os

application = Flask(__name__, static_folder="static")

KAKAO_JAVASCRIPT_KEY = os.getenv("kakao_javascript")
KAKAO_REST_API_KEY = os.getenv("kakao_reset")

@application.route('/')
def index():
    return render_template('main.html')

@application.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    num = request.form['num']
    database.save(name, num)
    return render_template('index.html')

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
