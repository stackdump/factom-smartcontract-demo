#!/usr/bin/env bash
echo 'Starting factomd'
# use logstash
factomd -count=1 -blktime=20 -network=LOCAL -startdelay=15 -logstash -logurl=127.0.0.1:8345 &> out.txt & 

#factomd -count=5 -blktime=20 -network=LOCAL -startdelay=15 &> out.txt &
echo -n $! > factomd.pid

echo "Waiting for factomd API to be up..."

while ! nc -z 127.0.0.1 8088; do   
  sleep 1
done

echo 'Starting factom-walletd'
factom-walletd &> wallet.txt &
echo -n $! > wallet.pid

echo "Waiting for walletd API to be up..."

while ! nc -z 127.0.0.1 8089; do   
  sleep 1
done

echo 'importing test wallet address:'
factom-cli importaddress Fs3E9gV6DXsYzf7Fqx1fVBQPQXV695eP3k5XbmHEZVRLkMdD9qCK # FA2jK2HcLnRdS94dEcU27rF3meoJfpUcZPSinpb7AwQvPRY6RL1Q
factom-cli importaddress Es3C7Ybmj8qoG1xZNrTm18EWKjW3BgvXQDFWZ1q1LvxxUBW5S5DL # EC3Hu1W7uMHf7CtSva1cMyr5rXKsu7rVqQtkJCDHqEV9dgh5FjAj
