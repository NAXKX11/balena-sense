FROM balenalib/raspberry-pi-alpine:3.11

RUN apk add influxdb

RUN sed -i 's|/var/lib/influxdb|/data/influxdb|g' /etc/influxdb/influxdb.conf

CMD influxd
