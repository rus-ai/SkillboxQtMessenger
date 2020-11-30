from datetime import datetime

import json
import requests
from PyQt5 import QtWidgets, QtCore, QtNetwork, QtMultimedia

import clientui

media_player = QtMultimedia.QMediaPlayer()
icq_url = QtCore.QUrl.fromLocalFile("icq-message.wav")
content = QtMultimedia.QMediaContent(icq_url)
media_player.setMedia(content)

class MessengerWindow(QtWidgets.QMainWindow, clientui.Ui_Messenger):
    def __init__(self, url):
        super().__init__()
        self.setupUi(self)

        self.url = url

        self.sendButton.pressed.connect(self.send_message)

        self.network = QtNetwork.QNetworkAccessManager()
        self.network.finished.connect(self.update_messages_request_ready)

        self.isNotRequested = True;

        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(1000)

    def update_messages(self):
        if self.isNotRequested:
            self.isNotRequested = False
            request = QtNetwork.QNetworkRequest(QtCore.QUrl(self.url + 'messages?after=' + str(self.after)))
            self.network.get(request)
        return

    def update_messages_request_ready(self, reply):
        js = json.loads(str(reply.readAll(), 'utf-8'))
        for message in js['messages']:
            dt = datetime.fromtimestamp(message['time'])
            dt = dt.strftime('%H:%M:%S')

            self.messagesBrowser.append(dt + ' ' + message['name'])
            self.messagesBrowser.append(message['text'])
            self.messagesBrowser.append('')
            self.repaint()

            self.after = message['time']
        self.isNotRequested = True

    def send_message(self):
        name = self.nameInput.text()
        text = self.textInput.toPlainText()
        media_player.play()
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
