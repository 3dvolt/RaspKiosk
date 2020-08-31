import os
import json
import requests
from flask import Flask, render_template,request,redirect,url_for
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/', methods=["GET", "POST"])
def index():
    file1 = open("SetId.txt", "r")
    id = file1.read()
    file1.close()
    if id != '':
        color = jsonreq(id)
        templateData = {
            'color': color}
        return render_template('list.html', **templateData)

@app.route('/selID', methods=["GET", "POST"])
def selID():
    color = ""
    templateData = {
        'color': color}
    return render_template('index.html', **templateData)

#http://192.168.8.153/selID

def jsonreq(id):
    url = 
    payload = {}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.request("GET", url, headers=headers, data=payload)
    y = json.loads(response.text)
    for num in range(len(y)):
        if y[num]['id'] == int(id):
            rotate = y[num]['']
            width = y[num]['']
            height = y[num]['']
            url = y[num]['']
            style = '<iframe src = "{}" style = "transform: rotate({}deg) ; height: {}px ; width: {}px ;" ></iframe>'.format(url, rotate, height, width)
            return style
    else:
        error = "NO ID FOUND"
        return error

@socketio.on('my event')
def custom_event(json, methods=['GET', 'POST']):
    if 'message' in str(json):
        if json['message'] != ' ':
            file1 = open("SetId.txt", "w")
            file1.write(json['message'])
            file1.close()
            socketio.emit('my response', json['message'])


if __name__ == '__main__':
    #app.secret_key = os.urandom(12)  # crypt
    #app.run(host='0.0.0.0', port=80, debug=False)
    socketio.run(app, debug=True, port=80)