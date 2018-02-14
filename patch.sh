for f in /usr/bin/gunicorn /usr/bin/gunicorn_django /usr/bin/gunicorn_paster; do
   sudo sed -i 's/python/python3/g' $f
   sudo sed -i 's/gunicorn==17.5/gunicorn==19.6.0/g' $f
done

sudo sed -i 's/python/python3/g' /usr/sbin/gunicorn-debian
sudo pip3 install --upgrade django


