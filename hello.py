import requests
import json

class TelegramBot:
    def __init__(self, token: str):
        self.token = token
        self.http_base = 'https://api.telegram.org/bot' + token + '/'
        r = requests.get(self.http_base + 'getMe')
        self.id = r.json()['result']['id']
        self.last_update_id = -1
    
    def process(self, json_ob):
        if json_ob['ok']:
            for el in json_ob['result']:
                if self.last_update_id != -1 and self.last_update_id >= el['update_id']:
                    continue
                self.last_update_id = el['update_id']
                if 'message' in el:
                    self.process_message(el['message'])

    def process_message(self, message):
        chat_id = message['chat']['id']
        message_id = message['message_id']
        payload = {'chat_id': chat_id, 'text': 'Hello World!', 'reply_to_message_id': message_id}
        print(message)
        print(self.last_update_id)
        if message['from']['id'] != self.id:
            r = requests.post(self.http_base + 'sendMessage', data=payload)

    def run(self):
        while True:
            r = requests.get(self.http_base + 'getUpdates')
            self.process(r.json())



token = '1367149259:AAH8aMAgGUbUCJs67rBp7R58Gn2zEAcLZL4'
bot = TelegramBot(token)
bot.run()
# http_base = 'https://api.telegram.org/bot' + token + '/'


# r = requests.get(http_base + 'getUpdates')

# js = r.json()

# print(js['ok'])

# for el in js['result']:
#     print(json.dumps(el, indent=4, sort_keys=True))
#     payload = {'chat_id': el['message']['chat']['id'], 'text': 'Hello World!'}
#     requests.post(http_base+'sendMessage', data=payload)