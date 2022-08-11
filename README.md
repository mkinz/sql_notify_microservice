This project aims to demonstrate a simple sql and email notification microservice.

A runner shell script (in this case, mailer.sh) calls the python app.

If the python app successfully connects to SQL, then it executes a SQL query and stores the output in an object.
main.py checks for a hash value of the queried data. If it's non-zero, then new data was found.
If data was found, then mailer.sh executes a mailer app (in this case, sendmail) to send the results to recipients.

mailer.sh is run on a job scheduler with regular frequency, and only mails if new data is found.


