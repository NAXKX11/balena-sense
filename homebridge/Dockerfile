FROM balenalib/raspberry-pi-python

WORKDIR /usr/src/app

RUN pip install influxdb web.py

COPY ./scripts ./scripts
RUN chmod +x scripts/*.py

CMD /usr/src/app/scripts/get_temperature.py
