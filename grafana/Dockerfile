FROM balenalib/raspberry-pi

RUN install_packages \
      fontconfig-config \
      fonts-dejavu-core \
      libfontconfig1 \
      ucf \
      jq \
      wget

COPY ./provisioning /usr/share/grafana/conf/provisioning
COPY ./*.sh /usr/src/app/
RUN chmod +x /usr/src/app/*.sh
RUN /usr/src/app/download.sh "raspberry-pi"

RUN dpkg -i /tmp/grafana.deb && rm /tmp/grafana.deb

CMD ["/bin/sh","/usr/src/app/entry.sh"]