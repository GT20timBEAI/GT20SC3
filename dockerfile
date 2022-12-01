# create your dockerfile here, for more information, read readme.md
FROM python:3.9-slim-buster
WORKDIR /app
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip3.9 install -r requirements.txt
COPY /app .
CMD ["flask","--app", "main", "run"]
