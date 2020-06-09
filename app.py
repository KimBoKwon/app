from flask import Flask, request, render_template, redirect, url_for, abort
app = Flask(__name__)

import game
import json
import dbdb

@app.route('/')
def index():
    return '메인페이지'

@app.route('/hello/')
def hello():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hellovar(name):
    dic = game.di(name)
    return render_template('gamestart.html', data=dic)

@app.route('/gamestart')
def gamestart():
    with open("static/save.txt", "r", encoding='utf-8') as f: 
        data = f.read() 
        dic = json.loads(data)
    return "{0}이 {1} 무기를 사용 해서 이겼다.".format(dic["name"], dic["weapon"])


@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        with open("static/save.txt", "r", encoding='utf-8') as f: 
            data = f.read() 
            dic = json.loads(data)
        return "{}이 {} 무기를 사용 해서 이겼다.".format(dic["name"], dic["weapon"])
    elif num == 2:
        return '도망갔다'
        

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login1', methods=['GET', 'POST'])
def login1():
    if request.method == 'GET':
        return 'GET으로 전송이다.'
    else:
        id = request.form['id']
        pw = request.form['pw']
        print(id, pw)
        ret = dbdb.select_user(id, pw)
        if ret != None:
            return "안녕하세요^^ {}님".format(id)
        else:
            return "아이디 패스워드를 확인하세요."

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
        dbdb.insert_data(num, name)
        return 'POST 이다. 학번은: {} 이름은: {}'.format(num, name)

@app.route('/getinfo')
def getinfo():
    ret = dbdb.select_all()
    print(ret)
    return render_template('getinfo.html', data=ret)
    # return '번호 : {}, 이름 : {}'.format(ret[0], ret[1])

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