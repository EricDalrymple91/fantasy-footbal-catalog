FROM python:3.10-slim-bullseye

EXPOSE 8080
ENV PYTHONPATH /ffcatalog

RUN apt-get update \
    && apt-get install -y \
    binutils \
    build-essential \
    cron\
    gdal-bin \
    git \
    libpq-dev \
    libproj-dev \
    sqlite3 \
    libsqlite3-dev  \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /ffcatalog

WORKDIR /ffcatalog

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ /ffcatalog

CMD ["/bin/bash"]
