web: gunicorn wotbuilds.wsgi:application --bind 0.0.0.0:$PORT
release: python manage.py collectstatic --noinput
web: gunicorn wotbuilds.wsgi:application