import json
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
  webhook_url = "https://discord.com/api/webhooks/1050943624021557278/FneLmdPZNeBtmlGmPqF2wJtUzoUBqc6mpXA3P2EsfUYrqaxX4CbEjZOy-Ou1JeVJmRG-"
  
  # Send the response to the Discord webhook
  requests.post(webhook_url, json=msg)
  
  return "OK"

if __name__ == '__main__':
  app.run()
