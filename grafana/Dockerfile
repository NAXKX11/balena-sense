FROM balenalib/raspberry-pi

COPY ./grafana.ini /usr/share/grafana/conf/custom.ini
COPY ./provisioning /usr/src/app/provisioning
COPY ./*.sh /usr/src/app/
RUN chmod +x /usr/src/app/*.sh

RUN install_packages \
      fontconfig-config \
      fonts-dejavu-core \
      libfontconfig1 \
      ucf \
      jq \
      wget

COPY ./download.sh /usr/src/app/download.sh
RUN chmod +x /usr/src/app/download.sh && /usr/src/app/download.sh raspberry-pi

RUN dpkg -i /tmp/grafana.deb && rm /tmp/grafana.deb

CMD ["/bin/sh","/usr/src/app/entry.sh"]
