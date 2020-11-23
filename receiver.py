import time
from datetime import datetime

import requests

after = 0

while True:
    response = requests.get(
        'http://127.0.0.1:5000/messages?after=' + str(after)
    )
    for message in response.json()['messages']:
        dt = datetime.fromtimestamp(message['time'])
        dt = dt.strftime('%H:%M:%S')

        print(dt, message['name'])
        print(message['text'])
        print()

        after = message['time']

    time.sleep(1)
