# ngo
Kind Heart charity NGO website project in Django 

# Setup Virtual Environment
* Create a new folder for Djnago Project
* Open windows powershell/ git bash/cmd

* install vertualenv
`pip install virtualenv`

* create vertualenv
`python -m venv env`

* Activate virtualenv 
`.\env\Scripts\activate`
(If not getting activated '`Set-ExecutionPolicy Unrestricted -Scope Process`')

# Setup Django Project
* Clone Project repo
`git clone https://github.com/ChetanR01/ngo.git`

* Move to project directory
`cd .\ngo\`

* install packages
`pip install django`
`pip install pillow`

* Make migrations 
`python manage.py migrate`

* Create a Superuser
`python manage.py createsuperuser`

* Run Django server
`python manage.py runserver`

* Open browser visit
`http://127.0.0.1:8000/admin`
