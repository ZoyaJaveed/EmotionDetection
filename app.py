import os
import random

from test import testing
from tweet import tweetFunction
from flask import Flask, render_template, flash, request, url_for
# from wtforms import Form, StringField, PasswordField, validators
from werkzeug.utils import redirect, secure_filename
from wtforms import Form, BooleanField, StringField, PasswordField, validators


DEBUG = False
app = Flask(__name__)
# app.config.from_object(__name__)
# app.config['SECRET_KEY'] = '123456'

usercredentials = {'admin': 'admin', 'swathi': 'swathi', 'zoya': 'zoya', 'ramya': 'ramya', 'sindhu': 'sindhu'}
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/test', methods=['POST'])
def test():
    print("Test in app.py")
    print(request.form["data"])
    result = testing(request.form["data"])
    print(result)
    print('done')
    return render_template('index.html')




@app.route('/tweet', methods=['POST'])
def tweet():
    print("Tweet in app.py")
    print(request.form["data"])
    emotionTest = request.form["data"]
    result = tweetFunction(emotionTest)
    print(result)
    print('done')
    return result


@app.route('/addEmotion', methods=['POST'])
def addEmotion():
    data = request.form["data"]
    emotion = request.form["emotion"]
    filePath = './learn/' + emotion + '/' + emotion + str(random.getrandbits(128)) + '.txt'

    with open(filePath, 'w') as f:
        f.write(data)

    print('done')
    return render_template('admin.html')


@app.route('/uploadHappyFile', methods=['POST'])
def uploadHappyFile():
    target = os.path.join(APP_ROOT, 'learn/happy/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("fileToUpload"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename.lower()])
        print(destination)
        file.save(destination)

    return render_template('admin.html')


@app.route('/uploadSadFile', methods=['POST'])
def uploadSadFile():
    target = os.path.join(APP_ROOT, 'learn/sad/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("fileToUpload"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template('admin.html')


@app.route('/uploadAngerFile', methods=['POST'])
def uploadAngerFile():
    target = os.path.join(APP_ROOT, 'learn/anger/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("fileToUpload"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template('admin.html')


@app.route('/uploadSurpriseFile', methods=['POST'])
def uploadSurpriseFile():
    target = os.path.join(APP_ROOT, 'learn/surprise/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("fileToUpload"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template('admin.html')


@app.route('/uploadFearFile', methods=['POST'])
def uploadFearFile():
    target = os.path.join(APP_ROOT, 'learn/fear/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("fileToUpload"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template('admin.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/')
def index():
    return render_template('index.html')


def execute(username, password):
    if usercredentials[username] == password:
        print("pass")
    else:
        print("false")


@app.route('/login', methods=['POST', 'GET'])
def login():
    username = request.form['username']
    password = request.form['password']
    execute(username, password)
    return redirect(url_for('admin'))


if __name__ == "__main__":
    app.run()
