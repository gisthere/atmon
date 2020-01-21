FROM grafana/grafana:6.6.0-beta1-ubuntu

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        phantomjs \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

USER grafana
