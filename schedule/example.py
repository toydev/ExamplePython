#!/usr/bin/env python

import schedule
import time

def frequent_job():
    print("frequent job")

def less_frequent_job():
    print("less frequent jog")

def hourly_job():
    print("hourly job")

def midnight_job():
    print("midnight job")

schedule.every(10).seconds.do(frequent_job)
schedule.every(3).minutes.do(less_frequent_job)
schedule.every().hour.do(hourly_job)
schedule.every().day.at("00:00").do(midnight_job)

while True:
    schedule.run_pending()
    time.sleep(1)
