FROM balenalib/raspberry-pi

COPY ./grafana.ini /usr/share/grafana/conf/custom.ini
COPY ./grafana.db /tmp

COPY ./start.sh /usr/src/app/start.sh

RUN install_packages \
      fontconfig-config \
      fonts-dejavu-core \
      libfontconfig1 \
      ucf

COPY ./download.sh /usr/src/app/download.sh
RUN chmod +x /usr/src/app/download.sh && /usr/src/app/download.sh raspberry-pi

RUN dpkg -i /tmp/grafana.deb && rm /tmp/grafana.deb

CMD ["/bin/sh","/usr/src/app/start.sh"]
