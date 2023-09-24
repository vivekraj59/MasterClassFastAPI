FROM ubuntu:trusty
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y sqlite3 libsqlite3-dev && \
    mkdir /db && \
    /usr/bin/sqlite3 /db/test.db
CMD /bin/bash

