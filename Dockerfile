FROM oneforone/backend-base
MAINTAINER 1For1
LABEL version="0.0.1"

ENV SCAN_FOLDER=/data

ADD requirements.txt /app/requirements.txt
ADD . /app
WORKDIR /app/

# TODO Add in pip -ie install .


# TODO Add in pip install for ofo_
#WORKDIR /app/ofo_backend
#RUN pip3 install -e . && pip install -e .
#WORKDIR /app/


# Install requirements
RUN pip3 install -r requirements.txt
