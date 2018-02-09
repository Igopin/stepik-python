sudo rm -f /etc/nginx/sites-enabled/*
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf

sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.hello.conf   /etc/gunicorn.d/hello.conf
sudo ln -s /home/box/web/etc/gunicorn.django.conf   /etc/gunicorn.d/django.conf
sudo /etc/init.d/gunicorn restart
