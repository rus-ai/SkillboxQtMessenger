from datetime import datetime

import requests
from PyQt5 import QtWidgets, QtCore

import clientui


class MessengerWindow(QtWidgets.QMainWindow, clientui.Ui_Messenger):
    def __init__(self, url):
        super().__init__()
        self.setupUi(self)

        self.url = url

        self.sendButton.pressed.connect(self.send_message)

        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(1000)

    def update_messages(self):
        try:
            response = requests.get(
                self.url + 'messages',
                params={'after': self.after}
            )
        except:
            return

        for message in response.json()['messages']:
            dt = datetime.fromtimestamp(message['time'])
            dt = dt.strftime('%H:%M:%S')

            self.messagesBrowser.append(dt + ' ' + message['name'])
            self.messagesBrowser.append(message['text'])
            self.messagesBrowser.append('')

            self.after = message['time']

    def send_message(self):
        name = self.nameInput.text()
        text = self.textInput.toPlainText()
        try:
            response = requests.post(
                self.url + 'send',
                json={'text': text, 'name': name}
            )
        except:
            self.messagesBrowser.append('Сервер недоступен. Попробуйте позднее')
            self.messagesBrowser.append('')
            self.messagesBrowser.repaint()
            return

        if response.status_code == 400:
            self.messagesBrowser.append('Не заполнены имя и/или текст')
            self.messagesBrowser.append('')
            self.messagesBrowser.repaint()
            return

        self.textInput.clear()
        self.textInput.repaint()


app = QtWidgets.QApplication([])
window = MessengerWindow('http://127.0.0.1:5000/')
window.show()
app.exec_()
