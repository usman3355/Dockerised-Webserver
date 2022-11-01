FROM ubuntu:22.04
FROM python:latest
WORKDIR /home/usman/Desktop/test_docker/test_server/database
RUN apt-get update
RUN apt install sudo
RUN sudo apt-get update && sudo apt-get dist-upgrade -y
RUN apt-get install -y --no-install-recommends apt-utils
RUN pip3 install mysql-connector-python
RUN apt-get install default-mysql-client -y
RUN apt-get install systemctl -y
RUN apt-get install vim -y
COPY entry.sh ./
COPY db.py ./
COPY webserver.py ./
COPY init.py ./
RUN chmod +x entry.sh
CMD [ "./entry.sh" ]