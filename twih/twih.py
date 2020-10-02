#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import argparse

MONTHS = {
    1: 'january',
    2: 'february',
    3: 'march',
    4: 'april',
    5: 'may',
    6: 'june',
    7: 'july',
    8: 'august',
    9: 'september',
    10: 'october',
    11: 'november',
    12: 'december',
    }


def fetch_week(START_DATE, MONTH):
    f = open('hlights.txt', 'w')
    date = START_DATE

    for _ in range(7):
        # setting url for site
        MONTH_NAME = MONTHS[MONTH]
        url = 'https://www.onthisday.com/events/' + str(MONTH_NAME) \
            + '/' + str(date)
        
        # fetching data
        req = requests.get(url,
                           allow_redirects=False).text.encode('ascii',
                'replace')

        # if given page doesn't exist, it redirects
        # so catch that, reset date and fetch data
        if not req:
            date = 1
            MONTH += 1
            if MONTH == 13:
                MONTH = 1
            MONTH_NAME = MONTHS[MONTH]
            url = 'https://www.onthisday.com/events/' + str(MONTH_NAME) \
                + '/' + str(date)
            req = requests.get(url,
                               allow_redirects=False).text.encode('ascii'
                    , 'replace')

        # forming soup object
        soup = BeautifulSoup(req, 'html.parser')

        # going thru each p tag
        for hlite in soup.find_all('p'):
            if hlite.text != 'Explore' and 'OnThisDay.com' \
                not in hlite.text:
                f.write(hlite.text + '\n')

        # for readability
        f.write('\n')
        # increment to next date
        date += 1

    # closing file
    f.close()


def main():
    # setting up argument parser
    ap = argparse.ArgumentParser(description='onthisday fetcher')
    ap.add_argument('-d', '--date',
                    help='the starting day in format DD.MM',
                    required=True)
    args = ap.parse_args()

    # fixing month and start date
    MONTH = int(args.date[3:5])
    START_DATE = int(args.date[:2])

    # call function
    fetch_week(START_DATE, MONTH)


if __name__ == '__main__':
    main()
