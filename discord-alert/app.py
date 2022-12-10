import json, os
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
  # Get the payload from the request
  payload = request.get_json()
  
  # Wrap the payload into a JSON object with the "msg" key
  msg = {"content": payload}
  
  # Set the URL for the Discord webhook
  webhook_url = os.environ.get('DISCORD_HOOK_URL')
  # Send the response to the Discord webhook
  requests.post(webhook_url, json=msg)
  
  return "OK"

if __name__ == '__main__':
  port = os.environ.get('FLASK_PORT') or 8080
  port = int(port)

  app.run(port=port,host='0.0.0.0')
