from flask import Flask, request

app = Flask(__name__)

VERIFICATION_TOKEN = '<>'
ACCESS_TOKEN = '<>'
Phone_Number_ID = "<>"

@app.route('/', methods=['GET'])
def index():
    return 'Simple WhatsApp Webhook tester<br>There is no front-end, see server.py for implementation!'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.verify_token') == VERIFICATION_TOKEN:
            return request.args.get('hub.challenge')
        else:
            return 'Invalid verification token'
    elif request.method == 'POST':
        data = request.json
        message = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
        print('Incoming webhook: ' + message)
        return 'Message received'

if __name__ == '__main__':
    app.run()
