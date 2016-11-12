sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart
sudo pkill gunicorn
gunicorn -b 0.0.0.0:8080 hello:app &
cd ~/web/ask
gunicorn -b 0.0.0.0:8000 ask.wsgi:application &
