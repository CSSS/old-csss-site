# Quick Instructions on Launching the CSSS Website #

The CSSS website can be launched through the following steps:

- SSH into the droplet
- Enter credentials for root access
- Enter the folder /opt/csssenv
- Enter the Python virtual environment: Run `source /opt/csssenv/bin/activate`
- Launching the website:  
  - DEV: `python manage.py runserver 104.236.189.54:8000`  
  - PROD: `/opt/csssenv/bin/gunicorn -c /opt/csssenv/csss-site/gunicorn_config.py cssssite.wsgi:application &`  

See the gunicorn documentation for more information on using gunicorn
