FROM balenalib/raspberry-pi-alpine:3.11

RUN apk add influxdb

RUN sed -i 's|/var/lib/influxdb|/data/influxdb|g' /etc/influxdb.conf
RUN mkdir /etc/influxdb
RUN cp /etc/influxdb.conf /etc/influxdb/

CMD ["influxd"]