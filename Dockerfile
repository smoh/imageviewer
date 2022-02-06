FROM python:3.9.10-slim-buster as compile-image

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential python3-dev apt-utils && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /opt/venv

# Create virtual environment
RUN python3 -m venv .

# Make sure virtualenv is used
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt ./
RUN pip install --upgrade pip && \
    pip3 install -r requirements.txt

# ---------------------------------------

FROM python:3.9.10-slim-buster as running-image

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    supervisor && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /opt/app
COPY . .
COPY --from=compile-image /opt/venv ./venv
RUN useradd appuser
RUN chown -R appuser /opt/app
COPY supervisord.conf /etc/
RUN chmod 0644 /etc/supervisord.conf

USER appuser
ENV PATH="/opt/app/venv/bin:$PATH"

CMD ["/usr/bin/supervisord"]
