FROM balenalib/raspberry-pi-python

WORKDIR /usr/src/app

COPY ./scripts ./scripts
RUN chmod +x scripts/*.py

CMD /usr/src/app/scripts/watchdog.py
