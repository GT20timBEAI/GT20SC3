# create your dockerfile here, for more information, read readme.md
FROM python:3.9-slim-buster
WORKDIR ./
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirement.txt requirement.txt
RUN pip3.9 install -r requirement.txt
COPY ./ .
CMD ["flask","--app", "main", "run"]
