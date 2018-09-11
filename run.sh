#!/usr/bin/env bash
echo 'Starting factomd'
factomd -count=5 -blktime=20 -network=LOCAL -startdelay=15 &> out.txt &
echo -n $! > factomd.pid
echo 'waiting 30s...'
sleep 30

echo 'Starting factom-walletd'
factom-walletd &> wallet.txt &
echo -n $! > wallet.pid

echo 'importing test wallet address:'
factom-cli importaddress Fs3E9gV6DXsYzf7Fqx1fVBQPQXV695eP3k5XbmHEZVRLkMdD9qCK
