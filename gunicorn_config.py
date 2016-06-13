import multiprocessing

command = "/opt/csssenv/bin/gunicorn"
pythonpath = "/opt/csssenv/csss-site"
bind = "127.0.0.1:8001"
workers = multiprocessing.cpu_count() * 2 + 1
