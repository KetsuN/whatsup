[uwsgi]
master = true
processes = 4
callable = app
http = 0.0.0.0:80
module = app
enable-threads = true
single-interpreter = true
die-on-term = true
harakiri = 180
harakiri-verbose = true
buffer-size = 65535
chdir = /code/
need-app = true
wsgi-disable-file-wrapper = true
{% if DEBUG %}python-autoreload = 1{% endif %}