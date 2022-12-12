import json, os
from flask import Flask, request, Response
from dhooks import Webhook

app = Flask(__name__)


@app.route('/1050943624021557278', methods=['POST'])
def webhook2():
  webhook_url = os.environ.get('DISCORD_HOOK_URL')
  hook = Webhook(webhook_url)
  a = json.dumps(request.json)
  print("*********raw json received**********")
  print(request.json)
  print("**************encoded string************")
  print(a)
  hook.send(a)
  return Response(status=200)

if __name__ == '__main__':
  port = os.environ.get('FLASK_PORT') or 8080
  port = int(port)

  app.run(port=port,host='0.0.0.0')