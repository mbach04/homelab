#!/bin/bash

WEBHOOK_URL="https://discord.com/api/webhooks/"

podman stop mc
podman rm mc
podman run --name mc -d -it -p 19132:19132/udp -p 25565:25565 -v ./data:/data:Z -e EULA=TRUE docker.io/itzg/minecraft-bedrock-server:latest


podman logs -f mc | \
while read line ; do
   echo "$line" | grep "Player"
   if [ $? = 0 ]
     then  
        MSG=`echo "$line" | grep -oP '(?<=INFO]).*?(?=,\ xuid:\ )'`
        JSON_STRING=$( jq -n \
          --arg un "MC-Logger" \
          --arg ct "$MSG" \
          '{username: $un, content: $ct}'
        )

        curl \
          -H "Content-Type: application/json" \
          -d "$JSON_STRING" \
          $WEBHOOK_URL
   fi
done &

