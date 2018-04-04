# Quick Instructions on Launching the CSSS Website #

The CSSS website can be launched through the following steps:

- SSH into the droplet
- Enter credentials for root access
- Enter the folder /opt/csssenv
- Run '/opt/csssenv/bin/gunicorn -c /opt/csssenv/csss-site/gunicorn_config.py cssssite.wsgi:application'

See the gunicorn documentation for more information on using gunicorn
