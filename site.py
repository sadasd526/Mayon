

import os
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

import json
from flask import Flask, render_template, redirect, url_for, request
from PIL import Image
from flask_cors import CORS
import base64
import openpyxl
from io import BytesIO
import requests

template_dir = os.path.abspath('')
app = Flask(__name__, template_folder=template_dir)
CORS(app)
data = json.loads(open('Python\data.json').read())

@app.route('/api/inventory')
def my():
    return json.loads(open('Python\my.json').read())

@app.route('/api/profile')
def profile():
    return json.loads(open('Python\data.json').read())

@app.route('/inventory')
def profile1():
    return render_template('inventory.html')
@app.route('/img/<imgn>')
def img(imgn):
    return redirect('https://starpets.gg/img/' + imgn)

@app.route('/goods/<path:mm>')
def goods(mm):
    print(mm)
    a = request.args.get('id')
    print(a)
    return redirect('https://goods.starpets.gg/api/assets/fetch?id=' + a)

@app.route('/api/user/get-country')
def gc():
    print()
    j = requests.get("https://geolocation-db.com/json/' + request.remote_addr + '&position=true").json()

    return '{"country": "'+j['country_code']+'", "city": "' + j['city'] + '"}'

    #https://127.0.0.1:8000/api/goods


#/api/best/products

@app.route('/api/best/products')
def best():
    return json.loads(open('items.json').read())

@app.route('/api/goods')
def goods1():
    print(request.data)
    return json.loads(open('goods.json').read())

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')