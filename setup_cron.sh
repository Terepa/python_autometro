#!/bin/bash

# Add the cron job to crontab
(crontab -l ; echo "* * * * *  /usr/local/bin/python3.11 /Users/dmittere/Desktop/local/python/process_data_xxx.py") | crontab -
