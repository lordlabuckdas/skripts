#!/usr/bin/bash
# copies file to home directory for persistence
cp mitm_checker.sh $HOME/
# get arp tables
arp -e | grep : | cut -d ' ' -f 1,21 > /tmp/init_arptab.txt
echo "added checker script to home directory"
# make it executable
chmod +x $HOME/mitm_checker.sh
# set up cronjob to check continuously
crontab cronjob.txt
echo "added cronjob"
echo "done setting up!"
