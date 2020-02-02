FROM python:3.7
ADD . /srv/chromecast-api
WORKDIR /srv/chromecast-api
RUN pip install --upgrade pip
RUN pip3 install -r requirements.lock
CMD uwsgi --ini uwsgi.ini