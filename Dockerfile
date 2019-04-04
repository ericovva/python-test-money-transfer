FROM python:3.7.3
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD /config/req.txt /config/
RUN pip install -r /config/req.txt
RUN pip install uwsgi
WORKDIR /opt/fintech_startup
CMD /opt/config/cmd.sh
