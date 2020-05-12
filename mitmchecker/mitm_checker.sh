#!/usr/bin/bash
arp -e | grep : | cut -d ' ' -f 1,21 > /tmp/cur_arptab.txt
if [ $(cat /tmp/cur_arptab.txt | head | cut -d  ' ' -f 2) != $(cat /tmp/init_arptab.txt | head | cut -d  ' ' -f 2) ];
then
	notify-send "ATTENTION!" "Under MITM attack!" -u critical
	echo "IP:	  Initial MAC:		Current MAC:"
	join /tmp/init_arptab.txt /tmp/cur_arptab.txt
fi
