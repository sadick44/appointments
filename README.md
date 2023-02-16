# appointments
This application is for users to settle appointment with sellers.
It is developped using python/django 

In order to use this application, you need to respect the following steps

1. Get to the master Branch and clone the project
2. Install virtual environment using the following syntax: virtualenv env
3. Connect to the virtualenv using: source env/bin/activate

Once all the steps are done successfully, you need the followings

a. In the terminal type: python manage.py makemigrations
b. python manage.py migrate

Then you need to execute the command that adds sellers in the database:

python manage.py user_creation

Then you are free to navigate through the website

#Further need if you need access to the admin panel to see the statistics:

python manage.py createsuperuser
username: admin
email:
password: admin 
