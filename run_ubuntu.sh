#!/bin/bash
# Sleep for 10 seconds before running migrations
echo 'sleep 10 secs'
sleep 10

python generate_sql.py

echo 'run db script'
# Define the number of retries

# Run your first command (e.g., flask db init)
echo 'run flask db init'
flask db init

# Run your second command (e.g., another command)
echo 'run flask db migrate'
flask db migrate -m "initial migration"

# Run your third command (e.g., yet another command)
echo run flask db upgrade
flask db upgrade

# Start your Flask application
echo 'start gunicorn server'
gunicorn app:app --bind 0.0.0.0:5005 #module_name:application_variable_name

#0.0.0.0: This is the host IP address.
#Using 0.0.0.0 means Gunicorn will listen on all available network interfaces,
# making the application accessible from outside the container.