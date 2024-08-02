from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

def login_success(name , age):
    if age>=18:
        return 'you can vote'
    else:
        return 'you cannot vote'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        ge = int(request.form['userage'])
        return login_success(name=user,age=ge)
    #else:
    #    user = request.args.get('username')
    #    return redirect(url_for('login_success', name=user))
    
if __name__ == '__main__':
    app.run()