from flask import Flask, request, render_template, redirect, url_for, abort
app = Flask(__name__)

@app.route('/')
def index():
    return '메인페이지'

@app.route('/hello/')
def hello():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hellovar(name):
    return 'Hello, {}!'.format(name)

@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        return '도라에몽'
    elif num == 2:
        return '진구'
    elif num == 3:
        return '퉁퉁이'
    else:
        return '없어요'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login1', methods=['GET', 'POST'])
def login1():
    if request.method == 'GET':
        return 'GET으로 전송이다.'
    else:
        id1 = request.form['id']
        pw = request.form['pw']
        print(id1, pw)
        if id1 == "abc" and pw == '1234':
            return '있는 계정입니다.'
        else:
            return '없는 계정입니다.'

@app.route('/form')
def form():
    return render_template('test.html')

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET으로 전송이다.'
    else:
        num = request.form['num'] #앞에 num은 저장할 변수 뒤에 num은 html에서 받아온 num값
        name = request.form['name']
        print(num, name)
        return 'POST 이다. 학번은: {} 이름은: {}'.format(num, name)

@app.route('/naver')
def naver():
    return redirect("http://www.naver.com/")

@app.route('/daum')
def daum(): 
    return redirect("http://www.daum.net/")

@app.route('/move/<site>')
def siter(site):
    if site == 'naver':
        return redirect(url_for('naver'))
    elif site == 'daum':
        return redirect(url_for('daum'))
    else:
        abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL를 확인하세요", 404

@app.route('/img')
def img():
    return render_template("image.html")


if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('daum'))
        print(url_for('naver'))
    app.run(debug=True)