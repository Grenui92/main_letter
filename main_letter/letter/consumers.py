import json

from channels.generic.websocket import WebsocketConsumer

class MainLetterConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):

        text_data_json = json.loads(text_data)
        input_text = text_data_json.get('input_text')

        self.send(text_data=json.dumps({'message': f'The letter you are looking for: {input_text}\n'}))