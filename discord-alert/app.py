import json, os
from flask import Flask, request, Response
from dhooks import Webhook

app = Flask(__name__)

@app.route('/1050943624021557278', methods=['POST'])
def webhook2():
  print(request.json)
  return Response(status=200)

@app.route('/', methods=['POST'])
def webhook():
  print(request.json)
  # Get the payload from the request
  payload = request.get_json()
  
  # Wrap the payload into a JSON object with the "msg" key
  #msg = {"content": payload}
  print(msg) 
  # Set the URL for the Discord webhook
  webhook_url = os.environ.get('DISCORD_HOOK_URL')
  # Send the response to the Discord webhook
  #requests.post(webhook_url, json=msg)
  hook = Webhook(webhook_url)
  print(hook)
  hook.send(payload)  
  return "OK"

if __name__ == '__main__':
  port = os.environ.get('FLASK_PORT') or 8080
  port = int(port)

  app.run(port=port,host='0.0.0.0')
