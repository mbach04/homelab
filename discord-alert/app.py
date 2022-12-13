import json, os
from flask import Flask, request, Response, requests
from dhooks import Webhook

app = Flask(__name__)

def is_proper_ip_subnet(client_ip):
  # Check if the IP address is within the 10.128.0.0/16 network
  if client_ip.startswith("10.128."):
    return True
  return False

@app.route('/1050943624021557278', methods=['POST'])
def webhook2():
    # Get the client's IP address
    if is_proper_ip_subnet(request.remote_addr):
      webhook_url = os.environ.get('DISCORD_HOOK_URL')
      hook = Webhook(webhook_url)
      a = json.dumps(request.json)
      print("********* raw json received **********")
      print(request.json)
      print("************** encoded string ************")
      print(a)
      #hook.send(a)
      discord_format = {"content": a}
      requests.post(webhook_url, json=discord_format)
      return Response(status=200)
    return Response(status=400)

if __name__ == '__main__':
  port = os.environ.get('FLASK_PORT') or 8080
  port = int(port)

  app.run(port=port,host='0.0.0.0')