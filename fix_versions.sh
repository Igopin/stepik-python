for f in /usr/bin/gunicorn /usr/bin/gunicorn_django /usr/bin/gunicorn_paster; do
   sed -i 's/python/python3/g' $f
   sed -i 's/gunicorn==17.5/gunicorn==19.6.0/g' $f
done

sed -i 's/python/python3/g' /usr/sbin/gunicorn-debian
