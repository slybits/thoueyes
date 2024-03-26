FROM alpine:latest

RUN apk update
RUN ["wget", "https://mirrors.aliyun.com/alpine/edge/main/aarch64/py3-jinja2-3.1.3-r0.apk", "-O", "/opt/py3-jinja2-3.1.3-r0.apk"]
RUN apk add python3
RUN apk add py3-flask
RUN apk add py3-requests
RUN apk add py3-regex
COPY index.py /opt/index.py
COPY templates /opt/templates
RUN apk add --allow-untrusted /opt/py3-jinja2-3.1.3-r0.apk
RUN rm /opt/py3-jinja2-3.1.3-r0.apk
EXPOSE 5000
ENV FLASK_APP=/opt/index.py
CMD ["flask", "run", "--host", "0.0.0.0"]
