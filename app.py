from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    return render_template('login.html')

@app.route('/<usr>')
def user(usr):
    return f'<h1>{usr}</h1>'

if __name__ == '__main__':
    app.run(debug=True)

# https://www.youtube.com/watch?v=4nzI4RKwb5I&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=4
