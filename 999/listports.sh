#!/bin/sh

IP=$(hostname -I)
first_port=6000
last_port=9999
echo "Scanning IP adr $IP from ports: $first_port to $last_port"
function scanner

{
for ((port=$first_port; port<=$last_port; port++))
        do
                (echo >/dev/tcp/$IP/$port)> /dev/null 2>&1 && echo $port open || echo "$port closed"
        done
}

scanner
