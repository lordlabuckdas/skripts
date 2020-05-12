#!/usr/bin/bash
cp mitm_checker.sh $HOME/
arp -e | grep : | cut -d ' ' -f 1,21 > /tmp/init_arptab.txt
echo "added checker script to home directory"
chmod +x $HOME/mitm_checker.sh
crontab cronjob.txt
echo "added cronjob"
echo "done setting up!"
