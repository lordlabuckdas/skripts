# mitm checker

* a script to check if user is under a mitm attack
* script checks for change in gateway mac, so false positives during network change occur
* sets up cron job for storing initial arp table values after boot up and checks for change every 2 minutes
* copies script to $HOME and stores arp tables in text files at /tmp/
* compatibility: linux, mac

### usage

> git clone https://github.com/lordlabuckdas/skripts.git ; cd skripts/mitmchecker
>
> chmod +x setup.sh mitm_checker.sh
>
> ./setup.sh

**note :** the cron job being set up overwrites the exisiting cron jobs. in case you want to add this cron job, copy the contents of [cronjob](./cronjob.txt), type ***crontab -e*** and paste them there after commenting out the corresponding line in [setup](./setup.sh)