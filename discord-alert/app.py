import json, os
import requests
from flask import Flask, request, Response

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
      a = json.dumps(request.json)
      print("********* raw json received **********")
      print(request.json)
      print("************** discord format ************")
      discord_format = json.dumps({"content": json.dumps(request.json)}, indent=4)
      print(discord_format)
      headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
      r = requests.post(webhook_url, json=discord_format, headers=headers)
      if r.ok:
        print("POST returned OK")
      else:
        print(r.status_code)
      return Response(status=200)
    return Response(status=400)

if __name__ == '__main__':
  port = os.environ.get('FLASK_PORT') or 8080
  port = int(port)

  app.run(port=port,host='0.0.0.0')