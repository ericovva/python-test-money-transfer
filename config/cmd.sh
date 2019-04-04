#!/bin/bash

yes | python manage.py collectstatic
pylint **/*.py --load-plugins pylint_django --max-parents=15
python manage.py migrate
python manage.py test
python manage.py create_accounts
uwsgi --ini /opt/config/uwsgi.ini;
