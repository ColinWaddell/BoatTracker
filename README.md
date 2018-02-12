# BoatTracker
For James

## Installing

Clone the repo and setup the virtualenv for this project:

    git clone git@github.com:ColinWaddell/BoatTracker.git boattracker
    cd boattracker
    virtualenv env
    source env/bin/active
    pip install -r requirements.txt

Build the database for the project:

    python manage.py migrate
    python manage.py makemigrations log
    python manage.py sqlmigrate log 0001
    python manage.py migrate
    python manage.py createsuperuser [fill out as required]

Everything should be good to run:

    python manage.py runserver 0.0.0.0:8000

Now if you can visit the dashboard at http://localhost:8000/

And if you want to update with a new reading the url is http://127.0.0.1:8000/log/update/[lat]/[lng]/[battery_v]/[pumping]

For example: http://127.0.0.1:8000/log/update/10.0/10.0/5.0/3.0

## Deploying
Don't use the ``runserver`` command to deploy this on your server. You'll have a bad time. [Instead setup uwsgi to work with your existing server](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-16-04). [Or deploy to AWS using something like Zappa](https://github.com/Miserlou/Zappa).