# Set up (not tested)
## Create a venv
`python3 -m venv venv`
`. venv/bin/activate`
## Install Django
`python -m pip install --upgrade pip`
`pip install -r requirements.txt`
## Start server
`python manage.py runserver`
## Import data
`python manage.py loaddata sbpow/fixtures/PlaceOfWorship.json`