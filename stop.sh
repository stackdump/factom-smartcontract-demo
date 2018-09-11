#!/usr/bin/env bash
# stop factomd & wallet services
kill `cat factomd.pid`
kill `cat wallet.pid`
rm *.pid
