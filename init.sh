unamestr=`uname`
if [[ "$unamestr" == 'Linux' ]]
then
	echo "Changing nginx config..."
	sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
	echo "Stopping nginx..."
	sudo /etc/init.d/nginx stop
	echo "Starting nginx again..."
	sudo /usr/sbin/nginx -c /etc/nginx/sites-enabled/test.conf
	echo "Changing Gunicorn config..."
	sudo ln -sf /home/box/web/etc/gunicorn.conf  /etc/gunicorn.d/test
	echo "Restarting gunicorn..."
	cd ~/web/ask
	sudo gunicorn -c /etc/gunicorn.d/test wsgi:application &
        # gunicorn -c ./etc/gunicorn.conf --chdir ask/ ask.wsgi
elif [[ "$unamestr" == 'vadym' ]]
then
	echo "Changing nginx config..."
	sudo ln -sf $HOME/workspace/projects/stepic/stepic-django/etc/nginx.conf  /usr/local/etc/nginx/test.conf
	echo "Stopping nginx..."
	sudo nginx -s stop
	echo "Starting nginx again..."
	sudo nginx -c /usr/local/etc/nginx/test.conf

	echo "Starting gunicorn..."
	sudo gunicorn -c ./etc/gunicorn.conf --chdir ask/ ask.wsgi
fi
