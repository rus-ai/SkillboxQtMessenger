import time
from datetime import datetime

from flask import Flask, request, abort

app = Flask(__name__)
load_time = datetime.now()

db = [
    {
        'text': 'Привет',
        'name': 'Nick',
        'time': time.time()
    }, {
        'text': 'Привет, Nick',
        'name': 'Jane',
        'time': time.time()
    }, {
        'text': 'Как дела?',
        'name': 'Nick',
        'time': time.time()
    }
]


@app.route("/")
def hello():
    return "Hello, World! <a href='/status'>Статистика</a>"


@app.route("/status")
def status():
    return {
        'status': True,
        'name': 'Messenger',
        'time1': time.time(),
        'time2': time.asctime(),
        'time3': datetime.now(),
        'time4': str(datetime.now()),
        'time5': datetime.now().strftime('%H:%M:%S %d/%m/%Y'),
        'time6': datetime.now().isoformat(),
        'time7 (wrong)': load_time
    }


@app.route("/send", methods=['POST'])
def send_message():
    if not isinstance(request.json, dict):
        return abort(400)

    text = request.json.get('text')
    name = request.json.get('name')
    if not isinstance(text, str) or not isinstance(name, str):
        return abort(400)
    if text == '' or name == '':
        return abort(400)

    db.append({
        'text': text,
        'name': name,
        'time': time.time()
    })
    return {'ok': True}


@app.route("/messages")
def get_messages():
    if 'after' in request.args:
        try:
            # проверка формата after
            after = float(request.args['after'])
        except:
            print('error')
            return abort(400)
    else:
        # дефолтное поведение
        after = 0

    filtered_db = []
    for message in db:
        if message['time'] > after:
            filtered_db.append(message)
            # pagination - чтобы возвращать сообщения партиями
            if len(filtered_db) >= 100:
                break

    return {'messages': filtered_db}


app.run()
