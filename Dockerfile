FROM python:latest
 
MAINTAINER melnyk12
 
WORKDIR /home/dfo
COPY . /home/dfo
RUN pip install -r requirements.txt
 
ENTRYPOINT ["start.py"]