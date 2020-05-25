# mini url

* shorten urls
* sourced from [bit.ly](https://bitly.com)
* copies link from clipboard and copies shortened url to clipboard
* requires [geckodriver](https://github.com/mozilla/geckodriver/releases) if using firefox as coded
* comment and uncomment the file accordingly
* added setup.sh file for linux users which installs geckodriver and adds it to PATH (/usr/local/bin)
* setup.sh makes **miniurl** a command for better accessibility
* new: made a crude workaround for executable and python call of miniurl, because of problems with ./miniurl call

### usage

1. if you want to run as a file

> git clone https://github.com/lordlabuckdas/skripts.git
>
> cd skripts/miniurl
>
> python3 -m pip install -r requirements.txt
>
> python3 miniurl.py

2. if you want to run as a command

> git clone https://github.com/lordlabuckdas/skripts.git
>
> cd skripts/miniurl
>
> chmod +x setup.sh
>
> miniurl ### will launch the program

**note :** have your link copied before running the program
