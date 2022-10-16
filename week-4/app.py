from flask import Flask
from flask import request 
from flask import redirect
from flask import render_template
from flask import session 

from pkg_resources import resource_listdir 

app = Flask(                    #建立Applicaiton 物件
    __name__, 
    static_folder='public', 
    static_url_path='/')   
app.secret_key = 'DavidLiu'     #設定密鑰

err1 = '?message=請輸入帳號、密碼'
err2 = '?message=帳號、或密碼輸入錯誤'
result = 0 

# 建立路徑 / 的函式處理方式
@app.route('/')
def index():
        return render_template('index.html')

# 建立路徑 /signin 的函式處理方式
@app.route('/signin', methods=['POST'])
def verify():
    account = request.form['account']
    password = request.form['password']
    if (account == 'test') & (password == 'test'):
        session['account'] = account
        return redirect('/member')
    elif (account == '') | (password == ''):
        return redirect('/error'+err1)
    elif (account != 'test') | (password != 'test'):
        return redirect('/error'+err2)

@app.route('/member')
def member():
    if 'account' not in session:
        return redirect('/')
    else: 
        return render_template('member.html')

@app.route('/error')
def error():
    msg = request.args.get('message')
    return render_template('error.html', message = msg)


@app.route('/signout')
def signOut():
    session.pop('account', None)
    return redirect('/')

@app.route('/square/<variable>', methods=['POST'])
def square(variable):
    final_result = int(variable) ** 2
    return render_template('calculation.html', result = final_result)


app.run(port = 3000)


    