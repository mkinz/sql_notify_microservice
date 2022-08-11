#!/bin/bash

echo "Starting..."

# who is getting the message?
recipients="matthew.kinzler@gmail.com"

# move to working directory
cd ~/PycharmProjects/sql_email_trigger/ || exit

# run code and store output in variable
EMAIL_REPORT=$(python main.py)

if [[ $EMAIL_REPORT ]]; then
  echo "Sending email report..."
  echo "$EMAIL_REPORT"
  #/usr/sbin/sendmail "$EMAIL_REPORT" $recipients
else
  echo "Email Report is Empty...Exiting"
  fi

echo "Done."