#!/bin/bash
echo "Setup NGINX and GUNICORN on this machine..."
echo "Create soft links to the /etc/ path nginx and gunicorn for setup config."
sudo ln -sf ~/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf ~/web/etc/hello.py /etc/gunicorn.d/hello.py

echo "Restart NGINX with new config."
sudo /etc/init.d/nginx restart

echo "Kill all previous jobs Gunicorn's for run apps with new configs"
sudo pkill gunicorn

echo "Run hello application on 0.0.0.0:8080!"
gunicorn -b 0.0.0.0:8080 hello:app &

echo "Go to the path ~/web/ask"
cd ~/web/ask
echo "Run ask application on 0.0.0.0:8000!"
gunicorn -b 0.0.0.0:8000 ask.wsgi:application &
